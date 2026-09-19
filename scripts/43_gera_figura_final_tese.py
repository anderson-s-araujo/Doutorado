import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("documentos/figuras", exist_ok=True)

# Dados limpos e reais das ferramentas consolidadas nos 11 estudos da tese
categorias = ["DMPOnline", "Repositório Institucional", "Repositório Nacional", "Moodle", "Não explicitado"]
frequencias = [4, 3, 2, 1, 1]

plt.figure(figsize=(9, 5))
barras = plt.barh(categorias, frequencias, color="#1b4f72", height=0.6)

plt.title("Plataformas e Ferramentas de PGD Mencionadas (S001-S011)", fontsize=11, fontweight="bold")
plt.xlabel("Frequência Absoluta (Número de Estudos)", fontsize=10)
plt.ylabel("Categoria / Ferramenta", fontsize=10)
plt.gca().invert_yaxis()

# Adicionar os valores numéricos exatos nas barras
for barra in barras:
    largura = barra.get_width()
    plt.text(largura + 0.1, barra.get_y() + barra.get_height()/2, f'{int(largura)}', 
             va='center', ha='left', fontsize=10, fontweight='bold')

plt.xlim(0, max(frequencias) + 1)
plt.tight_layout()

caminho_figura = "documentos/figuras/figura_resultado_ferramentas_tese.png"
plt.savefig(caminho_figura, dpi=300)
plt.close()

print("Figura definitiva gerada com sucesso!")
