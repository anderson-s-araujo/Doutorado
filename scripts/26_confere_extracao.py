import pandas as pd

caminho_csv = "dados/processados/extracao_estudos.csv"
df = pd.read_csv(caminho_csv)

print("=" * 80)
print("CONFERÊNCIA DOS DADOS EXTRAÍDOS DOS PDFS (Custos e Fatores Institucionais)")
print("=" * 80)

colunas_conferencia = ["study_id", "cost_factors", "contextual_institutional_factors"]
print(df[colunas_conferencia].to_string(index=False))
print("=" * 80)
