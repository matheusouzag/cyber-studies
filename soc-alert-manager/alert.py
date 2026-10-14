import json
from pathlib import Path
from datetime import datetime

caminho = Path(__file__).parent / "data" / "eventos_autenticacao.json"

def contar_eventos(api):
    sucesso = 0
    erro = 0
    with open(api, "r", encoding="utf-8") as f:
        entrada = json.load(f)

    for resultado in entrada:
        if resultado["resultado_autenticacao"] == "sucesso":
            sucesso += 1
        else:
            erro += 1

    return {
        "sucessos": sucesso,
        "falhas": erro
    }

def conversao_timezone(api):

    with open(api, "r", encoding="utf-8") as f:
            entrada = json.load(f)

    for tempo in entrada:
        print(datetime.fromisoformat(tempo["data_hora"]))

    return


print(contar_eventos(caminho))

print(conversao_timezone(caminho))