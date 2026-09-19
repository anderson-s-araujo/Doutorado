import pandas as pd

# Carregar a base de dados processada
caminho_csv = "dados/processados/extracao_estudos.csv"
df = pd.read_csv(caminho_csv)

print(f"Total de estudos analisados: {len(df)}\n")
print("=" * 50)

# Lista completa com todas as dimensões da análise aprofundada
colunas_analise = [
    "document_type",
    "knowledge_area",
    "support_actors_mentioned",
    "study_design",
    "dmp_context_and_requirement",
]

for coluna in colunas_analise:
    if coluna in df.columns:
        print(f"\nFrequência para: {coluna.upper()}")
        freq = df[coluna].value_counts(dropna=False)
        print(freq)
        print("-" * 50)
