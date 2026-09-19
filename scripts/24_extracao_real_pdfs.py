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
            
            # Exemplo prático de extração baseada em termos encontrados no texto
            # Aqui o script procura secções ou termos e extrai o contexto real
            linhas = texto_completo.split("\n")
            
            # Exemplo para practices_reported baseado no conteúdo real do PDF
            praticas_encontradas = []
            for linha in linhas:
                if any(termo in linha.lower() for termo in ["repository", "data sharing", "deposition", "metadata", "fair"]):
                    if len(linha.strip()) > 30: # Evita cabeçalhos curtos
                        praticas_encontradas.append(linha.strip())
            
            if praticas_encontradas:
                # Regista o primeiro trecho relevante encontrado no artigo real
                df.loc[mask, "practices_reported"] = praticas_encontradas[0][:200] # Limita o tamanho
            else:
                df.loc[mask, "practices_reported"] = "Não explicitado textualmente no PDF"
                
        except Exception as e:
            print(f"Erro ao ler o PDF {study_id}: {e}")
    else:
        print(f"PDF não encontrado para {study_id}")

df.to_csv(caminho_csv, index=False, encoding="utf-8")
print("Extração baseada nos PDFs reais concluída com sucesso!")
