import json
from pathlib import Path

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

    return sucesso, erro

print(contar_eventos(caminho))