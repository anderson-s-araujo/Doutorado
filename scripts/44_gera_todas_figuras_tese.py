import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("documentos/figuras", exist_ok=True)
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')

# --- FIGURA 1: Ferramentas e Plataformas de PGD ---
cat_ferramentas = ["DMPOnline", "Repositório Institucional", "Repositório Nacional", "Moodle", "Não explicitado"]
freq_ferramentas = [4, 3, 2, 1, 1]

plt.figure(figsize=(9, 5))
barras1 = plt.barh(cat_ferramentas, freq_ferramentas, color="#1b4f72", height=0.55)
plt.title("Plataformas e Ferramentas de PGD Mencionadas (S001-S011)", fontsize=11, fontweight="bold")
plt.xlabel("Frequência Absoluta (Número de Estudos)", fontsize=10)
plt.ylabel("Categoria / Ferramenta", fontsize=10)
plt.gca().invert_yaxis()

for barra in barras1:
    largura = barra.get_width()
    plt.text(largura + 0.1, barra.get_y() + barra.get_height()/2, f'{int(largura)}', 
             va='center', ha='left', fontsize=10, fontweight='bold')

plt.xlim(0, max(freq_ferramentas) + 1.5)
plt.tight_layout()
plt.savefig("documentos/figuras/figura_resultado_ferramentas_tese.png", dpi=300)
plt.close()

# --- FIGURA 2: Delineamento Metodológico dos Estudos ---
cat_delineamento = ["Revisão Sistemática", "Estudo de Caso", "Pesquisa Documental", "Ensaio Metodológico"]
freq_delineamento = [5, 3, 2, 1]

plt.figure(figsize=(9, 5))
barras2 = plt.barh(cat_delineamento, freq_delineamento, color="#117a65", height=0.55)
plt.title("Distribuição por Delineamento Metodológico (S001-S011)", fontsize=11, fontweight="bold")
plt.xlabel("Frequência Absoluta (Número de Estudos)", fontsize=10)
plt.ylabel("Delineamento", fontsize=10)
plt.gca().invert_yaxis()

for barra in barras2:
    largura = barra.get_width()
    plt.text(largura + 0.1, barra.get_y() + barra.get_height()/2, f'{int(largura)}', 
             va='center', ha='left', fontsize=10, fontweight='bold')

plt.xlim(0, max(freq_delineamento) + 1.5)
plt.tight_layout()
plt.savefig("documentos/figuras/figura_resultado_delineamentos_tese.png", dpi=300)
plt.close()

print("Todas as figuras analíticas definitivas foram geradas com sucesso!")
