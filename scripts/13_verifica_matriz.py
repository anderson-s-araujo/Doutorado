import pandas as pd

caminho_csv = "dados/processados/extracao_estudos.csv"
df = pd.read_csv(caminho_csv)

print("=" * 60)
print("VERIFICAÇÃO DO ESTADO ATUAL DA MATRIZ (S001 a S011)")
print("=" * 60)

# Selecionar colunas-chave para validação rápida
colunas_interesse = ["study_id", "practices_reported", "cost_factors"]
print(df[colunas_interesse].to_string(index=False))
print("=" * 60)
