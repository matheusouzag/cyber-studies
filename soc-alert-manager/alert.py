import json
from pathlib import Path
from datetime import datetime, timedelta
import ipaddress
import sys

def consumir_api(api):
    try:
        with open(api, "r", encoding="utf-8") as f:
            entrada = json.load(f)
        return entrada
    except FileNotFoundError:
        raise Exception(f"Erro: O arquivo '{api}' não foi encontrado.")
    except json.JSONDecodeError as e:
        raise Exception(f"Erro de Sintaxe JSON: {e.msg} na linha {e.lineno}")

def executar_validacao(api):
    print(f"Iniciando validação do arquivo: {api}")
    
    try:
        dados = consumir_api(api)
    except Exception as e:
        print(f"FALHA CRÍTICA: {e}")
        sys.exit(1)

    erros = validar_estrutura(dados)

    if erros:
        print("VALIDAÇÃO FALHOU. Erros encontrados:")
        for erro in erros:
            print(f"  - {erro}")
        sys.exit(1)
    else:
        return dados

def validar_estrutura(dados):
    erros = []

    if not isinstance(dados, list):
        erros.append("O JSON deve conter uma lista de eventos.")
        return erros

    for indice, evento in enumerate(dados):
        if not isinstance(evento, dict):
            erros.append(
                f"Evento {indice + 1}: deve ser um dicionário."
            )
            continue

        erros_evento = validar_evento(evento)

        for erro in erros_evento:
            erros.append(f"Evento {indice + 1}: {erro}")

    return erros

def validar_evento(dados):
    erros = []

    chaves_obrigatorias = ['usuario', 'ip_origem', 'data_hora', 'tipo_evento', 'resultado_autenticacao', 'justificativa']
    
    for chave in chaves_obrigatorias:
        if chave not in dados:
            erros.append(f"Chave obrigatória '{chave}' está ausente.")

    if 'usuario' in dados and not isinstance(dados['usuario'], str):
        erros.append("O campo 'usuario' deve ser uma string.")
    
    if 'ip_origem' in dados:
        try:
            ipaddress.ip_address(dados['ip_origem'])
        except ValueError: 
            erros.append("O campo 'ip_origem' deve conter um IP válido.")
        except TypeError: # ocorre quando não é um tipo válido
            erros.append("O campo 'ip_origem' deve ser uma string com um IP válido.")

    if 'data_hora' not in dados:
        erros.append("O campo 'data_hora' é obrigatório.")

    elif not isinstance(dados['data_hora'], str):
        erros.append("O campo 'data_hora' deve ser uma string.")

    else:
        try:
            data_hora = datetime.fromisoformat(dados['data_hora'])

            if data_hora.tzinfo is None:
                erros.append("O campo 'data_hora' deve conter um fuso horário.")

        except ValueError:
            erros.append("O campo 'data_hora' deve conter uma data e hora válidas.")


    if 'tipo_evento' in dados and not isinstance(dados['tipo_evento'], str):
        erros.append("O campo 'tipo_evento' deve ser uma string.")

    if 'resultado_autenticacao' not in dados:
        erros.append("O campo 'resultado_autenticacao' é obrigatório.")

    elif not isinstance(dados['resultado_autenticacao'], str):
        erros.append("O campo 'resultado_autenticacao' deve ser uma string.")

    elif dados['resultado_autenticacao'] not in ["sucesso", "falha"]:
        erros.append("O campo 'resultado_autenticacao' deve ser 'sucesso' ou 'falha'.")

    if "justificativa" in dados:
        justificativa = dados["justificativa"]

        if not isinstance(justificativa, str):
            erros.append("O campo 'justificativa' deve ser uma string.")
        elif not justificativa.strip():
            erros.append("O campo 'justificativa' não pode estar vazio.")

    return erros

def contar_eventos(retorno):
    sucesso = 0
    erro = 0

    for resultado in retorno:
        if resultado["resultado_autenticacao"] == "sucesso":
            sucesso += 1
        else:
            erro += 1

    return {
        "sucessos": sucesso,
        "falhas": erro
    }

def conversao_timezone(retorno):
    for i, tempo in enumerate(retorno):
        convertido = datetime.fromisoformat(tempo)
        retorno[i] = convertido

    return retorno

def verificar_falhas(retorno):
    usuarios_falha = [] 
    dict_justificativas_falha = {} 
    dict_contagem_falha = {}
    dict_horario_falha = {}

    for usuario in retorno:
        if usuario["resultado_autenticacao"] == "falha":
            if usuario["usuario"] not in usuarios_falha:
                usuarios_falha.append(usuario["usuario"])
            if usuario["usuario"] not in dict_justificativas_falha:
                dict_justificativas_falha[usuario["usuario"]] = []
                dict_horario_falha[usuario["usuario"]] = []
                dict_contagem_falha[usuario["usuario"]] = 0

            dict_justificativas_falha[usuario["usuario"]].append(usuario["justificativa"])
            dict_horario_falha[usuario["usuario"]].append(usuario["data_hora"])
            dict_contagem_falha[usuario["usuario"]] = dict_contagem_falha[usuario["usuario"]] + 1

    return dict_justificativas_falha, dict_contagem_falha, dict_horario_falha

def investigar_tempo(horario):
    conversao_timezone(horario)
    horario.sort(reverse=True)

    diferenca = horario[0] - horario[-1]

    if diferenca >= timedelta(minutes=5):
        print(diferenca)
        return False
    else:
        return True




def analisar_tempo(usuario, horario):
    for user, horario in horario.items():
        if usuario == user:
            resposta_tempo = investigar_tempo(horario)
            if resposta_tempo == True:
                return "5 falhas dentro de 5 minutos"
            else:
                return "Não ouve 5 falhas dentro de 5 minutos"

if __name__ == "__main__":
    caminho = Path(__file__).parent / "data" / "eventos_autenticacao.json"
    retorno_api = executar_validacao(caminho)

    #print(contar_eventos(retorno_api))
    #print(conversao_timezone(retorno_api))
    verificacao = verificar_falhas(retorno_api)
    horarios_falhas = verificacao[2]
    #print(horarios_falhas)

    for usuario, falha in verificacao[1].items():
        if falha >= 5:
            print(analisar_tempo(usuario, horarios_falhas))
    