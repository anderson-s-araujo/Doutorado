import os
import pandas as pd
from pypdf import PdfReader

caminho_csv = "dados/processados/extracao_estudos.csv"
pasta_pdfs = "dados/brutos/artigos_pdf"
df = pd.read_csv(caminho_csv)

# Dicionário de palavras-chave por coluna temática
categorias_busca = {
    "perceptions_summary": ["perception", "perceptions", "attitude", "view", "perceção", "percepção", "atitude"],
    "contextual_individual_factors": ["skill", "skills", "training", "awareness", "competência", "treinamento", "capacitação"],
    "facilitators_reported": ["facilitator", "support", "help", "facilitador", "suporte", "apoio"],
    "benefit_factors": ["benefit", "benefits", "advantage", "benefício", "vantagem"],
    "fair_knowledge": ["fair", "findable", "accessible", "interoperable", "reusable"],
    "tools_or_platforms_mentioned": ["repository", "zenodo", "figshare", "dspace", "platform", "ferramenta", "repositório"],
    "usability_user_experience": ["usability", "experience", "interface", "usabilidade", "experiência"]
}

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
            
            # Para cada coluna temática, busca o primeiro trecho relevante
            for coluna, termos in categorias_busca.items():
                if coluna in df.columns:
                    encontrados = []
                    for linha in linhas:
                        linha_lower = linha.lower()
                        if any(termo in linha_lower for termo in termos):
                            if len(linha.strip()) > 30:
                                encontrados.append(linha.strip())
                    
                    if encontrados:
                        df.loc[mask, coluna] = encontrados[0][:220]
                    else:
                        df.loc[mask, coluna] = "Não explicitado no PDF"
                        
        except Exception as e:
            print(f"Erro ao processar {study_id}: {e}")
    else:
        print(f"PDF não encontrado para {study_id}")

df.to_csv(caminho_csv, index=False, encoding="utf-8")
print("Extração multicritério baseada nos PDFs concluída com sucesso!")
