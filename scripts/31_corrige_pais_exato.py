import pandas as pd

caminho_csv = "dados/processados/extracao_estudos.csv"
df = pd.read_csv(caminho_csv)

print("Colunas detetadas no CSV:", df.columns.tolist())

# Identificar se existe alguma coluna parecida com country ou region
coluna_alvo = None
for col in df.columns:
    if "country" in col.lower() or "region" in col.lower() or "pais" in col.lower():
        coluna_alvo = col
        break

print(f"Coluna alvo identificada: {coluna_alvo}")

paises_dict = {
    "S001": "Estados Unidos",
    "S002": "Reino Unido",
    "S003": "Internacional",
    "S004": "Brasil",
    "S005": "Canadá",
    "S006": "Portugal",
    "S007": "Estados Unidos",
    "S008": "Espanha",
    "S009": "Países Baixos",
    "S010": "Reino Unido",
    "S011": "Brasil"
}

if coluna_alvo:
    for study_id, pais in paises_dict.items():
        df.loc[df["study_id"] == study_id, coluna_alvo] = pais
    df.to_csv(caminho_csv, index=False, encoding="utf-8")
    print(f"Sucesso! A coluna '{coluna_alvo}' foi atualizada.")
    print(df[["study_id", coluna_alvo]])
else:
    print("Erro: Nenhuma coluna correspondente a país/região foi encontrada no CSV.")
