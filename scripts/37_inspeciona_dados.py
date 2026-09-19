import pandas as pd

caminho_csv = "dados/processados/extracao_estudos.csv"
df = pd.read_csv(caminho_csv)

print("=" * 70)
print("INSPEÇÃO DOS DADOS DA COLUNA DE FERRAMENTAS")
print("=" * 70)
if "tools_or_platforms_mentioned" in df.columns:
    print(df[["study_id", "tools_or_platforms_mentioned"]])
else:
    print("Coluna não encontrada.")
print("=" * 70)
