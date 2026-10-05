"""Gera index.html a partir de src/template.html e dos dados em data/,
e atualiza a lista de fontes do README.md.

Uso: python src/build.py
"""
import json, os, re

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FORA = {"carreira", "eleicao"}


def carrega(nome):
    d = json.load(open(os.path.join(RAIZ, "data", nome), encoding="utf-8"))
    ev = [e for e in d["eventos"]
          if e["categoria"] not in FORA
          and not e.get("marco_legal", "").startswith(("PL ", "PEC "))]
    d["eventos"] = sorted(ev, key=lambda e: e["data"], reverse=True)
    print(nome, len(ev), "itens")
    return d


def data_br(s):
    return "/".join(reversed(s.split("-")))


def tabela_fontes(d):
    linhas = ["| Data | Item | Fonte |", "|---|---|---|"]
    for e in d["eventos"]:
        titulo = (e.get("titulo_simples") or e["titulo"]).replace("|", "\\|")
        if e["categoria"] == "controversia":
            titulo += " (caso na Justiça)"
        fonte = e["fonte"]
        linhas.append(f"| {data_br(e['data'])} | {titulo} | [{fonte['nome'].replace('|', '-')}]({fonte['url']}) |")
    return "\n".join(linhas)


lula, flavio = carrega("lula.json"), carrega("flavio.json")

tpl = open(os.path.join(RAIZ, "src", "template.html"), encoding="utf-8").read()
corpo = (tpl.replace("@@LULA@@", json.dumps(lula, ensure_ascii=False, indent=2))
            .replace("@@FLAVIO@@", json.dumps(flavio, ensure_ascii=False, indent=2)))
pagina = ('<!doctype html>\n<html lang="pt-BR">\n<head>\n<meta charset="utf-8">\n'
          '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
          '</head>\n<body>\n' + corpo + '\n</body>\n</html>\n')
open(os.path.join(RAIZ, "index.html"), "w", encoding="utf-8").write(pagina)
print("index.html gerado")

readme_path = os.path.join(RAIZ, "README.md")
readme = open(readme_path, encoding="utf-8").read()
fontes = ("<!-- fontes:inicio -->\n"
          "_Lista gerada por `src/build.py` a partir de `data/`. Não edite à mão._\n\n"
          f"### Lula\n\n{tabela_fontes(lula)}\n\n"
          f"### Flávio Bolsonaro\n\n{tabela_fontes(flavio)}\n"
          "<!-- fontes:fim -->")
readme = re.sub(r"<!-- fontes:inicio -->.*?<!-- fontes:fim -->", lambda m: fontes, readme, flags=re.S)
open(readme_path, "w", encoding="utf-8").write(readme)
print("README.md atualizado")
