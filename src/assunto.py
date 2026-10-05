"""Grava o campo `assunto` em data/*.json (usado na visao "Por assunto").

A classificacao e editorial e segue o mesmo criterio para os dois candidatos:
o assunto principal de que a lei ou o programa trata. Casos na Justica ficam
no assunto proprio "Casos na Justiça".

Uso: python src/assunto.py
"""
import json, os

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ASSUNTO = {
    # Lula
    "Auxílio Gás do Povo": "Ajuda em dinheiro",
    "Criação do Bolsa Família": "Ajuda em dinheiro",
    "Novo Bolsa Família": "Ajuda em dinheiro",
    "Isenção de IR para renda até R$ 5 mil": "Impostos, dívidas e contas do governo",
    "Regulamentação da reforma tributária": "Impostos, dívidas e contas do governo",
    "Novo arcabouço fiscal": "Impostos, dívidas e contas do governo",
    "Desenrola Brasil": "Impostos, dívidas e contas do governo",
    "Brasil fora do Mapa da Fome da ONU": "Comida e agricultura",
    "Plano Brasil Sem Fome": "Comida e agricultura",
    "Alimentação escolar e agricultura familiar": "Comida e agricultura",
    "Lei Orgânica de Segurança Alimentar": "Comida e agricultura",
    "Lei da Agricultura Familiar": "Comida e agricultura",
    "Ministério do Desenvolvimento Social": "Comida e agricultura",
    "Programa de Aquisição de Alimentos (PAA)": "Comida e agricultura",
    "Lançamento do Fome Zero": "Comida e agricultura",
    "Programa Agora Tem Especialistas": "Saúde",
    "Mais Médicos reformulado": "Saúde",
    "Farmácia Popular": "Saúde",
    "Aliança Global contra a Fome e a Pobreza": "Relação com outros países",
    "Criação do Pé-de-Meia": "Educação",
    "Atualização da Lei de Cotas": "Educação",
    "Programa Escola em Tempo Integral": "Educação",
    "Criação dos Institutos Federais": "Educação",
    "Piso salarial nacional do magistério": "Educação",
    "Regulamentação do Fundeb": "Educação",
    "Plano de Metas da educação e Reuni": "Educação",
    "Criação do ProUni": "Educação",
    "Política de valorização do salário mínimo": "Trabalho, salário e negócios",
    "Lei de igualdade salarial": "Trabalho, salário e negócios",
    "Criação do Microempreendedor Individual": "Trabalho, salário e negócios",
    "Simples Nacional": "Trabalho, salário e negócios",
    "Lançamento do Novo PAC": "Obras, energia e transporte",
    "Lançamento do PAC": "Obras, energia e transporte",
    "Programa Luz para Todos": "Obras, energia e transporte",
    "Retomada do Minha Casa, Minha Vida": "Moradia",
    "Criação do Minha Casa, Minha Vida": "Moradia",
    "Estatuto da Igualdade Racial": "Direitos e proteção",
    "Lei Maria da Penha sancionada": "Direitos e proteção",
    "Estatuto do Idoso sancionado": "Direitos e proteção",
    # Flavio
    "Lei sobre presídio federal para quem mata policial": "Segurança e Justiça",
    "Lei que restringe as saídas temporárias de presos": "Segurança e Justiça",
    "Lei de apoio psicológico a policiais": "Segurança e Justiça",
    "Lei prevê multa por trote a serviços de emergência": "Segurança e Justiça",
    "Lei veda cargo público a condenado por pedofilia": "Segurança e Justiça",
    "Nova Lei Geral do Turismo": "Trabalho, salário e negócios",
    "Lei do teletrabalho e do auxílio-alimentação": "Trabalho, salário e negócios",
    "Lei dispensa certidão de crédito para servidor": "Trabalho, salário e negócios",
    "Lei garante acesso a motivo de reprovação psicológica": "Trabalho, salário e negócios",
    "Lei das assembleias virtuais em condomínios": "Serviços e vida civil",
    "Lei sobre assinaturas eletrônicas e receitas": "Serviços e vida civil",
    "Lei autoriza criação da NAV Brasil": "Obras, energia e transporte",
    "Lei permite nome do bebê na certidão de natimorto": "Direitos e proteção",
    "Lei reduz jornada de pais de pessoas com deficiência": "Direitos e proteção",
    "Lei autoriza programa de recifes artificiais": "Meio ambiente, animais e desastres",
    "Lei cria programa para animais perdidos": "Meio ambiente, animais e desastres",
    "Lei sobre serviços funerários em desastres": "Meio ambiente, animais e desastres",
    "Lei cria semana de prevenção a desastres": "Meio ambiente, animais e desastres",
    "Lei obriga farmácias a informar sobre genéricos": "Saúde",
    "Lei inclui dentistas no controle de infecção hospitalar": "Saúde",
    "Lei sobre laqueadura e vasectomia gratuitas": "Saúde",
    "Lei garante matrícula a filhos de agentes mortos": "Educação",
}

usados = set()
for nome in ("lula.json", "flavio.json"):
    p = os.path.join(RAIZ, "data", nome)
    d = json.load(open(p, encoding="utf-8"))
    sem = []
    for e in d["eventos"]:
        if e["categoria"] == "controversia":
            e["assunto"] = "Casos na Justiça"
        elif "abrangencia" in e:
            if e["titulo"] in ASSUNTO:
                e["assunto"] = ASSUNTO[e["titulo"]]
                usados.add(e["titulo"])
            else:
                sem.append(e["titulo"])
    json.dump(d, open(p, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=2)
    print(nome, "sem assunto:", sem or "nenhum")
print("mapeados e nao usados:", set(ASSUNTO) - usados or "nenhum")
