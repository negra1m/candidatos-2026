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

O comando gera o `index.html` e atualiza a lista de fontes abaixo.

## Fontes

Principais origens dos dados: legislação do Palácio do Planalto (planalto.gov.br), legislação da Assembleia Legislativa do Rio de Janeiro (Alerj), Senado Federal, Tribunal Superior Eleitoral (TSE), Supremo Tribunal Federal (STF), Agência Brasil, Agência Senado, Nações Unidas Brasil e o site oficial da Aliança Global contra a Fome e a Pobreza. Os dois pedidos de investigação sem desdobramento (Vorcaro e atuação junto aos EUA) usam o Correio Braziliense, e as respostas dos candidatos nesses dois casos vêm da CNN Brasil.

Fonte de cada item mostrado na página:

<!-- fontes:inicio -->
_Lista gerada por `src/build.py` a partir de `data/`. Não edite à mão._

### Lula

| Data | Item | Fonte |
|---|---|---|
| 23/09/2026 | Pedido ao Supremo para investigar Lula (caso na Justiça) | [Correio Braziliense](https://www.correiobraziliense.com.br/politica/2026/09/7507140-flavio-apresenta-noticia-crime-contra-lula-por-relacao-com-vorcaro.html) |
| 09/2026 | Justiça Eleitoral aceita processo contra Lula (caso na Justiça) | [Tribunal Superior Eleitoral](https://www.tse.jus.br/comunicacao/noticias/2026/Setembro/tse-pede-informacoes-complementares-antes-de-analisar-acao-de-flavio-bolsonaro-contra-lula-e-alckmin) |
| 07/2026 | Lula multado em 15 mil reais por propaganda (caso na Justiça) | [Agência Brasil](https://agenciabrasil.ebc.com.br/politica/noticia/2026-07/tre-sp-multa-lula-por-propaganda-eleitoral-antecipada-cabe-recurso) |
| 13/02/2026 | Auxílio Gás do Povo: ajuda com o gás de cozinha | [Planalto - Legislação](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/lei/l15348.htm) |
| 02/2026 | Desfile sobre Lula: Justiça Eleitoral não barra (caso na Justiça) | [Tribunal Superior Eleitoral](https://www.tse.jus.br/comunicacao/noticias/2026/Fevereiro/tse-nega-liminares-em-acoes-sobre-desfile-de-escola-de-samba-em-homenagem-ao-presidente-lula) |
| 26/11/2025 | Sem Imposto de Renda para quem ganha até 5 mil | [Planalto - Legislação](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15270.htm) |
| 07/2025 | Brasil sai do Mapa da Fome das Nações Unidas | [Nações Unidas Brasil](https://brasil.un.org/pt-br/299851-artigo-brasil-voltou-sair-do-mapa-da-fome) |
| 30/05/2025 | Atendimento com especialista na saúde pública | [Planalto - Legislação (Lei 15.233/2025)](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15233.htm) |
| 16/01/2025 | Novas regras dos impostos sobre o que se compra | [Planalto - Legislação](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214.htm) |
| 18/11/2024 | Aliança de países contra a fome e a pobreza | [Global Alliance against Hunger and Poverty](https://globalallianceagainsthungerandpoverty.org/new/world-leaders-launch-the-global-alliance-against-hunger-and-poverty-2/) |
| 16/01/2024 | Poupança para aluno pobre do ensino médio | [Planalto - Legislação](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2024/lei/l14818.htm) |
| 13/11/2023 | Vagas reservadas em escolas e faculdades federais | [Planalto - Legislação](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14723.htm) |
| 31/08/2023 | Plano Brasil Sem Fome: combate à fome | [Planalto - Legislação](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/decreto/d11679.htm) |
| 30/08/2023 | Novas regras para os gastos do governo | [Planalto - Legislação](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp200.htm) |
| 28/08/2023 | Regra para aumentar o salário mínimo | [Planalto - Legislação](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14663.htm) |
| 11/08/2023 | Novo programa de obras públicas pelo país | [Planalto - Legislação](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/decreto/D11632.htm) |
| 31/07/2023 | Mais horas por dia na escola pública | [Planalto - Legislação](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14640.htm) |
| 03/07/2023 | Salário igual para mulheres e homens | [Planalto - Legislação](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14611.htm) |
| 05/06/2023 | Ajuda para fazer acordo de dívida atrasada | [Planalto - Legislação (Lei 14.690/2023)](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14690.htm) |
| 20/03/2023 | Mais Médicos muda e passa a formar especialistas | [Planalto - Legislação (Lei 14.621/2023)](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14621.htm) |
| 02/03/2023 | Bolsa Família volta com novo jeito de calcular | [Planalto - Legislação (Lei 14.601/2023)](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14601.htm) |
| 14/02/2023 | Volta do Minha Casa, Minha Vida | [Planalto - Legislação (Lei 14.620/2023)](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14620.htm) |
| 20/07/2010 | Lei de igualdade para a população negra | [Planalto - Legislação](https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2010/lei/l12288.htm) |
| 16/06/2009 | Merenda com comida de pequenos agricultores | [Planalto - Legislação](https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2009/lei/l11947.htm) |
| 25/03/2009 | Minha Casa, Minha Vida: ajuda para ter casa | [Planalto - Legislação (MP 459/2009)](https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2009/mpv/459.htm) |
| 29/12/2008 | Novas escolas federais para ensinar uma profissão | [Planalto - Legislação](https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2008/lei/l11892.htm) |
| 19/12/2008 | Criação do Microempreendedor Individual | [Planalto - Legislação](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp128.htm) |
| 16/07/2008 | Piso de salário para professor de escola pública | [Planalto - Legislação](https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2008/lei/l11738.htm) |
| 20/06/2007 | Dinheiro para escolas públicas e professores | [Planalto - Legislação](https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2007/lei/l11494.htm) |
| 24/04/2007 | Metas para escolas e crescimento das universidades | [Planalto - Legislação (Decreto 6.096/2007)](https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2007/decreto/d6096.htm) |
| 22/01/2007 | Programa de obras públicas pelo país | [Planalto - Legislação](https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2007/decreto/d6025.htm) |
| 14/12/2006 | Jeito próprio de pequena empresa pagar imposto | [Planalto - Legislação](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp123.htm) |
| 15/09/2006 | Lei do direito de todos a comer bem | [Planalto - Legislação](https://www.planalto.gov.br/ccivil_03/_ato2004-2006/2006/lei/l11346.htm) |
| 07/08/2006 | Proteção para mulher que sofre violência em casa | [Planalto - Legislação](https://www.planalto.gov.br/ccivil_03/_ato2004-2006/2006/lei/l11340.htm) |
| 24/07/2006 | Lei para os pequenos agricultores | [Planalto - Legislação](https://www.planalto.gov.br/ccivil_03/_ato2004-2006/2006/lei/l11326.htm) |
| 13/01/2005 | Bolsa de estudo em faculdade particular | [Planalto - Legislação](https://www.planalto.gov.br/ccivil_03/_ato2004-2006/2005/lei/l11096.htm) |
| 13/05/2004 | Lei inclui ministério de combate à fome | [Planalto - Legislação](https://www.planalto.gov.br/ccivil_03/_ato2004-2006/2004/lei/l10.869.htm) |
| 13/04/2004 | Farmácia Popular: ajuda para conseguir remédios | [Planalto - Legislação](https://www.planalto.gov.br/ccivil_03/_ato2004-2006/2004/lei/l10.858.htm) |
| 11/11/2003 | Luz elétrica para casas que não tinham | [Planalto - Legislação](https://www.planalto.gov.br/ccivil_03/decreto/2003/d4873.htm) |
| 20/10/2003 | Bolsa Família: dinheiro para famílias pobres | [Planalto - Legislação (MP 132/2003)](https://www.planalto.gov.br/ccivil_03/mpv/antigas_2003/132.htm) |
| 01/10/2003 | Direitos para quem tem 60 anos ou mais | [Planalto - Legislação](https://www.planalto.gov.br/ccivil_03/leis/2003/l10.741.htm) |
| 02/07/2003 | Governo compra comida de pequenos agricultores | [Planalto - Legislação](https://www.planalto.gov.br/ccivil_03/leis/2003/l10.696.htm) |
| 01/2003 | Fome Zero: governo contra a fome | [Planalto - Legislação (Lei 10.683/2003)](https://www.planalto.gov.br/ccivil_03/leis/2003/l10.683.htm) |

### Flávio Bolsonaro

| Data | Item | Fonte |
|---|---|---|
| 01/09/2026 | Vídeo que imita Bolsonaro: Justiça não dá multa (caso na Justiça) | [Agência Brasil](https://agenciabrasil.ebc.com.br/justica/noticia/2026-09/tse-rejeita-acao-para-derrubar-imagem-de-bolsonaro-feita-por-ia) |
| 09/2026 | Justiça Eleitoral aceita processo contra Flávio (caso na Justiça) | [Tribunal Superior Eleitoral](https://www.tse.jus.br/comunicacao/noticias/2026/Setembro/corregedoria-geral-eleitoral-solicita-informacoes-ao-facebook-e-a-shopee-sobre-perfis-investigados) |
| 13/07/2026 | Moraes suspende visitas de Flávio ao pai (caso na Justiça) | [Agência Brasil](https://agenciabrasil.ebc.com.br/justica/noticia/2026-07/moraes-suspende-visitas-de-flavio-bolsonaro-na-prisao-domiciliar) |
| 07/2026 | Justiça Eleitoral manda tirar vídeo de Flávio (caso na Justiça) | [Agência Brasil](https://agenciabrasil.ebc.com.br/politica/noticia/2026-08/tse-determina-remocao-de-video-que-associa-lula-ao-pcc-e-ao-cv) |
| 29/05/2026 | Pedidos de investigação após reunião com Trump (caso na Justiça) | [Correio Braziliense](https://www.correiobraziliense.com.br/politica/2026/06/7432269-juristas-pedem-a-pgr-investigacao-de-flavio-por-atentado-a-soberania.html) |
| 11/05/2026 | Prisão federal para quem mata agente de segurança | [Agência Senado](https://www12.senado.leg.br/noticias/materias/2026/05/12/sancionado-o-uso-de-presidios-federais-para-assassinos-de-agentes-de-seguranca) |
| 05/2026 | Investigação sobre dinheiro de Vorcaro para filme (caso na Justiça) | [Agência Brasil](https://agenciabrasil.ebc.com.br/justica/noticia/2026-09/mendonca-incluiu-flavio-bolsonaro-como-investigado-no-caso-dark-horse) |
| 04/2026 | Investigação por suposta calúnia contra Lula (caso na Justiça) | [Agência Brasil](https://agenciabrasil.ebc.com.br/justica/noticia/2026-07/em-manifestacao-escrita-flavio-bolsonaro-nega-ter-caluniado-lula) |
| 18/09/2024 | Novas regras para o turismo | [Agência Senado](https://www12.senado.leg.br/noticias/materias/2024/06/05/aprovada-atualizacao-da-lei-geral-do-turismo-texto-retorna-para-a-camara) |
| 11/04/2024 | Lei limita a saída temporária de presos | [Agência Senado](https://www12.senado.leg.br/noticias/materias/2024/02/20/senado-aprova-restricao-as-saidinhas-de-presos-texto-volta-para-a-camara) |
| 02/09/2022 | Trabalho a distância e auxílio-alimentação | [Agência Senado](https://www12.senado.leg.br/noticias/materias/2022/08/03/aprovada-mp-que-regulamenta-teletrabalho-e-muda-auxilio-alimentacao) |
| 08/03/2022 | Reunião de condomínio pela internet | [Agência Senado](https://www12.senado.leg.br/noticias/materias/2022/02/15/Assembleias-virtuais-em-condominios-seguem-a-sancao) |
| 19/10/2020 | Caso das rachadinhas na Assembleia do Rio (caso na Justiça) | [Supremo Tribunal Federal](https://noticias.stf.jus.br/postsnoticias/stf-rejeita-dois-recursos-do-ministerio-publico-do-rj-no-caso-das-rachadinhas/) |
| 23/09/2020 | Assinatura eletrônica para falar com o governo | [Senado Federal - ficha da matéria](https://www25.senado.leg.br/web/atividade/materias/-/materia/142535) |
| 19/11/2019 | Empresa pública para serviços de navegação aérea | [Senado Federal - ficha da matéria](https://www25.senado.leg.br/web/atividade/materias/-/materia/135031) |
| 29/04/2019 | Apoio psicológico para policiais e suas famílias | [Alerj - Legislação estadual](https://alerjln1.alerj.rj.gov.br/contlei.nsf/c8aa0900025feef6032564ec0060dfff/4a72d52a364bb0d7832583ef006ea93b?OpenDocument) |
| 30/11/2018 | Bebê que nasce sem vida ganha nome na certidão | [Alerj - Legislação estadual](https://alerjln1.alerj.rj.gov.br/contlei.nsf/c8aa0900025feef6032564ec0060dfff/e5bdbd6b25114b5b03258359005f1169?OpenDocument) |
| 02/03/2018 | Recifes artificiais no litoral do Rio | [Alerj - Legislação estadual](https://alerjln1.alerj.rj.gov.br/contlei.nsf/c8aa0900025feef6032564ec0060dfff/d5e8bbe982b65fcc832582480057a7af?OpenDocument) |
| 22/09/2017 | Fotos na internet para achar animal perdido | [Alerj - Legislação estadual](https://alerjln1.alerj.rj.gov.br/contlei.nsf/c8aa0900025feef6032564ec0060dfff/5d0d62ba260a1e32832581a7005fca71?OpenDocument) |
| 31/10/2016 | Multa para trote nos telefones de emergência | [Alerj - Legislação estadual](https://alerjln1.alerj.rj.gov.br/contlei.nsf/c8aa0900025feef6032564ec0060dfff/159007a40fd4f0a98325805e00597c1e?OpenDocument) |
| 18/10/2016 | Menos horas para quem cuida de pessoa com deficiência | [Alerj - Legislação estadual](https://alerjln1.alerj.rj.gov.br/contlei.nsf/c8aa0900025feef6032564ec0060dfff/bbfbb39bce93e9fc83258051005b964c?OpenDocument) |
| 14/10/2014 | Serviço funerário em desastres no estado do Rio | [Alerj - Legislação estadual](https://alerjln1.alerj.rj.gov.br/contlei.nsf/c8aa0900025feef6032564ec0060dfff/5b13a75a806ed8f183257d74006044f3?OpenDocument) |
| 22/05/2014 | Sem emprego público a condenado por abuso de menor | [Alerj - Legislação estadual](https://alerjln1.alerj.rj.gov.br/contlei.nsf/c8aa0900025feef6032564ec0060dfff/a77aa3d6454d6b4883257ce1006a6945?OpenDocument) |
| 22/11/2013 | Farmácia deve avisar sobre remédio genérico | [Alerj - Legislação estadual](https://alerjln1.alerj.rj.gov.br/contlei.nsf/c8aa0900025feef6032564ec0060dfff/73c7ad12d0b510d083257c30005abfe8?OpenDocument) |
| 07/11/2013 | Dentistas no combate à infecção em hospitais | [Alerj - Legislação estadual](https://alerjln1.alerj.rj.gov.br/contlei.nsf/c8aa0900025feef6032564ec0060dfff/584ea8e60854605883257c1d0058b37b?OpenDocument) |
| 12/09/2011 | Semana para prevenir desastres no estado do Rio | [Alerj - Legislação estadual](https://alerjln1.alerj.rj.gov.br/contlei.nsf/c8aa0900025feef6032564ec0060dfff/e76b90fda282cc958325790b005b7743?OpenDocument) |
| 04/04/2011 | Reprovado em teste psicológico pode saber o motivo | [Alerj - Legislação estadual](https://alerjln1.alerj.rj.gov.br/contlei.nsf/c8aa0900025feef6032564ec0060dfff/5da79ec4ccb52c47832578680071af1f?OpenDocument) |
| 08/12/2006 | Cirurgia grátis para não ter mais filhos no Rio | [Alerj - Legislação estadual](https://alerjln1.alerj.rj.gov.br/contlei.nsf/c8aa0900025feef6032564ec0060dfff/e364ec91f38f5bd383257242006868a6?OpenDocument) |
| 21/06/2004 | Vaga na escola para filhos de agentes mortos | [Alerj - Legislação estadual](https://alerjln1.alerj.rj.gov.br/contlei.nsf/c8aa0900025feef6032564ec0060dfff/5aacd46ba577c4f983256ebb006214b9?OpenDocument) |
| 29/12/2003 | Emprego público no Rio sem exigir nome limpo | [Alerj - Legislação estadual](https://alerjln1.alerj.rj.gov.br/contlei.nsf/c8aa0900025feef6032564ec0060dfff/1f9608d4396e67de83256e0c0067bbf5?OpenDocument) |
<!-- fontes:fim -->

## Fotos

- Lula: "Foto oficial de Luiz Inácio Lula da Silva (2023–2027)", Palácio do Planalto, CC BY 2.0, via Wikimedia Commons.
- Flávio Bolsonaro: "Foto oficial do senador Flávio Bolsonaro", Agência Senado, via Wikimedia Commons.
