# Projeto de Doutoramento: Extração e Análise de Dados de Revisão

[![DOI](https://zenodo.org/badge/1375773992.svg)](https://doi.org/10.5281/zenodo.22875538)

Este repositório contém os dados, ficheiros de extração e scripts de suporte ao projeto de doutoramento desenvolvido no PPGICS/Fiocruz, focado em governança de dados, Planos de Gestão de Dados (DMP) e princípios FAIR na investigação em saúde.

## Estrutura do Diretório

- \dados/\:
  - \Brutos/\: Ficheiros PDF dos estudos incluídos (\S001.pdf\ a \S011.pdf\) e exportações originais (Rayyan).
  - \processados/\: Matrizes consolidadas de extração (\extracao_estudos.csv\).
  - \
Resultados/\: Tabelas cruzadas e dados sintetizados.
- \documentos/\: Notas metodológicas, protocolos e figuras analíticas (\documentos/figuras/\).
- \scripts/\: Rotinas em Python para validação, população de matrizes e geração de gráficos analíticos.

## Ambiente de Execução

- Gestor de ambiente e dependências: \uv\ / Python 3.12
- Exemplos de execução:
  \\\powershell
  uv run python scripts/03_popula_extracao.py
  uv run --with pandas --with matplotlib python scripts/46_gera_figuras_adicionais.py
  \\\

## Licença

Este repositório é distribuído sob os termos da licença constante no ficheiro [LICENSE](LICENSE).

## Citação

Para referenciar os scripts e dados deste projeto, consulte o ficheiro [CITATION.cff](CITATION.cff) ou utilize o DOI persistente: [10.5281/zenodo.22875538](https://doi.org/10.5281/zenodo.22875538).
