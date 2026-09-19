import os
from pypdf import PdfReader

pasta_pdfs = "dados/brutos/artigos_pdf"

for i in range(1, 12):
    study_id = f"S0{i:02d}"
    caminho_pdf = os.path.join(pasta_pdfs, f"{study_id}.pdf")
    
    if os.path.exists(caminho_pdf):
        print("=" * 60)
        print(f"ESTUDO: {study_id}")
        print("=" * 60)
        try:
            reader = PdfReader(caminho_pdf)
            print(f"Total de páginas: {len(reader.pages)}")
            
            # Extrair texto das primeiras 3 páginas (resumo, introdução e metodologia inicial)
            texto_inicial = ""
            for page_num in range(min(3, len(reader.pages))):
                texto_inicial += reader.pages[page_num].extract_text() or ""
            
            print("Prévia do texto (Resumo / Metodologia):")
            print(texto_inicial[:800] + "...\n")
        except Exception as e:
            print(f"Erro ao ler {study_id}: {e}")
