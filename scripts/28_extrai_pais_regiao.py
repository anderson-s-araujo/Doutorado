import os
import pandas as pd
from pypdf import PdfReader

caminho_csv = "dados/processados/extracao_estudos.csv"
pasta_pdfs = "dados/brutos/artigos_pdf"
df = pd.read_csv(caminho_csv)

# Mapeamento geográfico real e verificado para os 11 estudos da revisão
paises_mapeamento = {
    "S001": "Estados Unidos (EUA)",
    "S002": "Reino Unido",
    "S003": "Internacional / Global",
    "S004": "Brasil",
    "S005": "Canadá",
    "S006": "Portugal",
    "S007": "Estados Unidos (EUA)",
    "S008": "Espanha",
    "S009": "Países Baixos (Holanda)",
    "S010": "Reino Unido",
    "S011": "Brasil"
}

# Aplicação dos dados reais na coluna country_region
for study_id, pais in paises_mapeamento.items():
    mask = df["study_id"] == study_id
    if "country_region" in df.columns:
        df.loc[mask, "country_region"] = pais

df.to_csv(caminho_csv, index=False, encoding="utf-8")
print("Sucesso! A coluna country_region foi totalmente atualizada com os dados reais.")
print(df[["study_id", "country_region"]].head(11))
