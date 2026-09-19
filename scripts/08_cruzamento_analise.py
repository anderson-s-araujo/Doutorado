import pandas as pd

# Carregar a base de dados processada
caminho_csv = "dados/processados/extracao_estudos.csv"
df = pd.read_csv(caminho_csv)

print("=" * 60)
print("ANÁLISE E CRUZAMENTO DE VARIÁVEIS DA TESE")
print("=" * 60)

# 1. Mapeamento Metodológico (study_design)
print("\n--- 1. Distribuição de Desenhos de Estudo (study_design) ---")
print(df["study_design"].value_counts(dropna=False))

# 2. Contextualização dos Requisitos de PDM (dmp_context_and_requirement)
print("\n--- 2. Distribuição de Requisitos de PDM (dmp_context_and_requirement) ---")
print(df["dmp_context_and_requirement"].value_counts(dropna=False))

# 3. Cruzamento: Desenho de Estudo x Requisitos de PDM
print("\n--- 3. Cruzamento: Desenho de Estudo vs Requisitos de PDM ---")
cruzamento_1 = pd.crosstab(df["study_design"], df["dmp_context_and_requirement"], margins=True)
print(cruzamento_1)

# 4. Cruzamento: Atores de Suporte x Requisitos de PDM
print("\n--- 4. Cruzamento: Atores de Suporte vs Requisitos de PDM ---")
cruzamento_2 = pd.crosstab(df["support_actors_mentioned"], df["dmp_context_and_requirement"], margins=True)
print(cruzamento_2)
print("=" * 60)
