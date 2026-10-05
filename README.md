# Qual candidato fez o que?

Página que compara, lado a lado, as leis e os programas de Lula (PT) e Flávio Bolsonaro (PL), candidatos no 2º turno da eleição presidencial de 25 de outubro de 2026, e os casos dos dois na Justiça.

Os textos estão em linguagem simples. Cada item traz a lei e a fonte pública para quem quiser conferir.

## Regras (iguais para os dois candidatos)

- **Leis e programas:** entram só os que já valem (leis sancionadas, decretos e programas em vigor). Projetos que ainda não viraram lei, cargos e eleições não entram.
- **Casos na Justiça:** casos de outubro de 2024 a outubro de 2026, ou casos mais antigos que tiveram novidade nesse período, em que o próprio candidato é alvo de investigação, processo ou decisão de órgão público. Também entram dois pedidos de investigação sem desdobramento: Vorcaro (Lula) e atuação junto aos EUA (Flávio). Estar na lista não indica culpa; cada item mostra em que pé está o caso.
- **Temas (Família, Soberania do país, Segurança, Combate à pobreza):** a classificação é editorial e segue a regra mostrada em cada botão da página.
- **"Para que serve":** descreve o objetivo geral daquele tipo de lei, como valeria em qualquer país, sem avaliar resultado.

Dados atualizados em 5 de outubro de 2026.

## Estrutura

```
index.html          página pronta (abre direto no navegador ou no GitHub Pages)
lula.jpg            foto oficial (Palácio do Planalto, CC BY 2.0)
flavio.jpg          foto oficial (Agência Senado, atribuição obrigatória)
data/lula.json      dados de Lula
data/flavio.json    dados de Flávio Bolsonaro
src/template.html   modelo da página
src/build.py        gera o index.html a partir do modelo e dos dados
```

Cada item em `data/*.json` guarda o texto técnico original (`titulo`, `descricao`, `status`) e a versão em linguagem simples (`titulo_simples`, `texto_simples`, `status_simples`), além da fonte (`fonte.url`). Os arquivos também têm eventos de carreira, eleição e projetos não aprovados, que o build deixa fora da página.

## Atualizar a página

Depois de editar `data/*.json` ou `src/template.html`:

```
python src/build.py
```

## Fotos

- Lula: "Foto oficial de Luiz Inácio Lula da Silva (2023–2027)", Palácio do Planalto, CC BY 2.0, via Wikimedia Commons.
- Flávio Bolsonaro: "Foto oficial do senador Flávio Bolsonaro", Agência Senado, via Wikimedia Commons.
