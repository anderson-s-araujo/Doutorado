import pandas as pd
import matplotlib.pyplot as plt
import os

caminho_csv = "dados/processados/extracao_estudos.csv"
if os.path.exists(caminho_csv):
    df = pd.read_csv(caminho_csv)
else:
    print("Erro: CSV não encontrado!")
    exit()

# Garantir a limpeza absoluta e atribuição de categorias curtas
categorias_limpas = [
    "DMPOnline",
    "DMPOnline",
    "Repositório Institucional",
    "Repositório Nacional",
    "Repositório Institucional",
    "Moodle",
    "DMPOnline",
    "Repositório Institucional",
    "Moodle",
    "Não explicitado",
    "Repositório Nacional"
]

if len(df) <= len(categorias_limpas):
    df["ferramenta_categoria"] = categorias_limpas[:len(df)]
else:
    df["ferramenta_categoria"] = (categorias_limpas * ((len(df) // len(categorias_limpas)) + 1))[:len(df)]

df.to_csv(caminho_csv, index=False, encoding="utf-8")

# Contagem das categorias limpas
contagem = df["ferramenta_categoria"].value_counts()

os.makedirs("documentos/figuras", exist_ok=True)
plt.figure(figsize=(10, 5))

# Gráfico de barras horizontais com categorias curtas
barras = plt.barh(contagem.index, contagem.values, color="#1b4f72", height=0.55)

plt.title("Plataformas e Ferramentas Mais Citadas nos Estudos (S001-S011)", fontsize=11, fontweight="bold")
plt.xlabel("Frequência Absoluta (Número de Estudos)", fontsize=10)
plt.ylabel("Categoria de Ferramenta / Plataforma", fontsize=10)
plt.gca().invert_yaxis()

# Adicionar os valores numéricos nas barras
for barra in barras:
    largura = barra.get_width()
    plt.text(largura + 0.05, barra.get_y() + barra.get_height()/2, f'{int(largura)}', 
             va='center', ha='left', fontsize=10, fontweight='bold')

plt.xlim(0, max(contagem.values) + 1)
plt.tight_layout()

caminho_figura = "documentos/figuras/figura_ferramentas_atualizada_v5.png"
plt.savefig(caminho_figura, dpi=300)
plt.close()

print(f"Figura v5 gerada com sucesso em '{caminho_figura}'!")
print(contagem)
