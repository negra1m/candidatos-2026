"""Gera index.html a partir de src/template.html e dos dados em data/.

Uso: python src/build.py
"""
import json, os

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FORA = {"carreira", "eleicao"}


def carrega(nome):
    d = json.load(open(os.path.join(RAIZ, "data", nome), encoding="utf-8"))
    ev = [e for e in d["eventos"]
          if e["categoria"] not in FORA
          and not e.get("marco_legal", "").startswith(("PL ", "PEC "))]
    d["eventos"] = sorted(ev, key=lambda e: e["data"], reverse=True)
    print(nome, len(ev), "itens")
    return json.dumps(d, ensure_ascii=False, indent=2)


tpl = open(os.path.join(RAIZ, "src", "template.html"), encoding="utf-8").read()
corpo = tpl.replace("@@LULA@@", carrega("lula.json")).replace("@@FLAVIO@@", carrega("flavio.json"))
pagina = ('<!doctype html>\n<html lang="pt-BR">\n<head>\n<meta charset="utf-8">\n'
          '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
          '</head>\n<body>\n' + corpo + '\n</body>\n</html>\n')
open(os.path.join(RAIZ, "index.html"), "w", encoding="utf-8").write(pagina)
print("index.html gerado")
