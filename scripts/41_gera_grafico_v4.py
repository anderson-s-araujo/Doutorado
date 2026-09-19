import pandas as pd
import matplotlib.pyplot as plt
import os

caminho_csv = "dados/processados/extracao_estudos.csv"
df = pd.read_csv(caminho_csv)

# Contagem exata das categorias
contagem = df["ferramenta_categoria"].value_counts()

os.makedirs("documentos/figuras", exist_ok=True)
plt.figure(figsize=(9, 5))

# Gráfico de barras horizontais simples e direto
barras = plt.barh(contagem.index, contagem.values, color="#1b4f72", height=0.6)

plt.title("Distribuição Consolidada de Ferramentas e Plataformas (S001-S011)", fontsize=11, fontweight="bold")
plt.xlabel("Frequência Absoluta (Número de Estudos)", fontsize=10)
plt.ylabel("Categoria de Ferramenta / Plataforma", fontsize=10)
plt.gca().invert_yaxis()

# Adicionar os valores numéricos nas barras
for barra in barras:
    largura = barra.get_width()
    plt.text(largura + 0.1, barra.get_y() + barra.get_height()/2, f'{int(largura)}', 
             va='center', ha='left', fontsize=10, fontweight='bold')

plt.xlim(0, max(contagem.values) + 1.5)
plt.tight_layout()

caminho_figura = "documentos/figuras/figura_ferramentas_atualizada_v4.png"
plt.savefig(caminho_figura, dpi=300)
plt.close()

print(f"Figura v4 gerada com sucesso em '{caminho_figura}'!")
print(contagem)
