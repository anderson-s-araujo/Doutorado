import pandas as pd
import os

caminho_csv = "dados/processados/extracao_estudos.csv"
df = pd.read_csv(caminho_csv)

print("=" * 80)
print("TABELA 1: CARACTERIZAÇÃO GERAL DOS ESTUDOS (S001 - S011)")
print("=" * 80)

colunas_tabela1 = [col for col in ["study_id", "country_region", "study_design", "participant_count"] if col in df.columns]
tabela1_md = df[colunas_tabela1].to_markdown(index=False)
print(tabela1_md)
print("\n" + "=" * 80)

os.makedirs("documentos", exist_ok=True)
caminho_saida = "documentos/tabelas_resultados_tese.md"
with open(caminho_saida, "w", encoding="utf-8") as f:
    f.write("# Tabelas de Resultados da Tese (Dados Reais)\n\n")
    f.write("## Tabela 1: Caracterização Geral dos Estudos\n\n")
    f.write(tabela1_md)
    f.write("\n\n")

print(f"Tabelas geradas e guardadas com sucesso em '{caminho_saida}'!")
