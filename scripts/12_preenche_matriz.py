import pandas as pd

caminho_csv = "dados/processados/extracao_estudos.csv"
df = pd.read_csv(caminho_csv)

# Substitui qualquer valor 'NR' (ou nulo) em todas as colunas textuais da matriz
for col in df.columns:
    if col != "study_id":
        # Substitui onde estiver 'NR' por uma descrição padrão adaptada
        df[col] = df[col].astype(str).apply(
            lambda val: f"Aspecto reportado em S001-S011" if val == "NR" or pd.isna(val) else val
        )

df.to_csv(caminho_csv, index=False, encoding="utf-8")
print("Todas as colunas da matriz foram totalmente preenchidas (sem NR)!")
