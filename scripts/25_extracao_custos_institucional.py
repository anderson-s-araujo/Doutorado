import os
import pandas as pd
from pypdf import PdfReader

caminho_csv = "dados/processados/extracao_estudos.csv"
pasta_pdfs = "dados/brutos/artigos_pdf"
df = pd.read_csv(caminho_csv)

for i in range(1, 12):
    study_id = f"S0{i:02d}"
    caminho_pdf = os.path.join(pasta_pdfs, f"{study_id}.pdf")
    mask = df["study_id"] == study_id
    
    if os.path.exists(caminho_pdf):
        try:
            reader = PdfReader(caminho_pdf)
            texto_completo = ""
            for pagina in reader.pages:
                texto_completo += (pagina.extract_text() or "") + "\n"
            
            linhas = texto_completo.split("\n")
            
            # 1. Busca por fatores de custo
            custos_encontrados = []
            for linha in linhas:
                linha_lower = linha.lower()
                if any(termo in linha_lower for termo in ["cost", "costs", "expense", "funding", "financial", "recurso", "custo", "financiamento"]):
                    if len(linha.strip()) > 25:
                        custos_encontrados.append(linha.strip())
            
            if custos_encontrados:
                df.loc[mask, "cost_factors"] = custos_encontrados[0][:220]
            else:
                df.loc[mask, "cost_factors"] = "Não mencionado explicitamente"

            # 2. Busca por fatores institucionais
            institucional_encontrado = []
            for linha in linhas:
                linha_lower = linha.lower()
                if any(termo in linha_lower for termo in ["institution", "institutional", "policy", "policies", "university", "política", "institucional", "diretriz"]):
                    if len(linha.strip()) > 25:
                        institucional_encontrado.append(linha.strip())
            
            if institucional_encontrado:
                df.loc[mask, "contextual_institutional_factors"] = institucional_encontrado[0][:220]
            else:
                df.loc[mask, "contextual_institutional_factors"] = "Não mencionado explicitamente"

        except Exception as e:
            print(f"Erro ao processar {study_id}: {e}")
    else:
        print(f"Ficheiro PDF não encontrado para {study_id}")

df.to_csv(caminho_csv, index=False, encoding="utf-8")
print("Extração de custos e fatores institucionais concluída com base nos PDFs reais!")
