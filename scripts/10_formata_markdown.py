import pandas as pd

# Carregar a base de dados processada
caminho_csv = "dados/processados/extracao_estudos.csv"
df = pd.read_csv(caminho_csv)

print("=" * 60)
print("TABELAS CRUZADAS FORMATADAS EM MARKDOWN")
print("=" * 60)

# 1. Cruzamento: Desenho de Estudo x Requisitos de PDM
print("\n### Tabela: Desenho de Estudo vs Requisitos de PDM\n")
cruzamento_1 = pd.crosstab(df["study_design"], df["dmp_context_and_requirement"])
print(cruzamento_1.to_markdown())

# 2. Cruzamento: Atores de Suporte x Requisitos de PDM
print("\n\n### Tabela: Atores de Suporte vs Requisitos de PDM\n")
cruzamento_2 = pd.crosstab(df["support_actors_mentioned"], df["dmp_context_and_requirement"])
print(cruzamento_2.to_markdown())
print("\n" + "=" * 60)
