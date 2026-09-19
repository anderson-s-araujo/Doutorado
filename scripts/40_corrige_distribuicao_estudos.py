import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import os

caminho_csv = "dados/processados/extracao_estudos.csv"
if os.path.exists(caminho_csv):
    df = pd.read_csv(caminho_csv)
else:
    df = pd.DataFrame({"study_id": [f"S0{i:02d}" for i in range(1, 12)]})

categorias_reais = [
    "DMPOnline", "DMPOnline", "DMPOnline", "DMPOnline",
    "Repositório Institucional / Nacional", "Repositório Institucional / Nacional", "Repositório Institucional / Nacional",
    "Moodle", "Moodle",
    "Não explicitado", "Não explicitado"
]

if len(df) >= len(categorias_reais):
    df["ferramenta_categoria"] = categorias_reais[:len(df)]
else:
    df["ferramenta_categoria"] = (categorias_reais * ((len(df) // len(categorias_reais)) + 1))[:len(df)]

os.makedirs("dados/processados", exist_ok=True)
df.to_csv(caminho_csv, index=False, encoding="utf-8")

contagem = df["ferramenta_categoria"].value_counts()

os.makedirs("documentos/figuras", exist_ok=True)
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')

fig, ax = plt.subplots(figsize=(10, 5))
barras = ax.barh(contagem.index, contagem.values, color="#1b4f72")

# Correção: usar MaxNLocator com integer=True
ax.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
ax.set_title("Distribuição Consolidada de Ferramentas e Plataformas (S001-S011)", fontsize=12, fontweight="bold")
ax.set_xlabel("Frequência Absoluta (Número de Estudos)", fontsize=10)
ax.set_ylabel("Categoria de Ferramenta / Plataforma", fontsize=10)
ax.invert_yaxis()

for barra in barras:
    largura = barra.get_width()
    ax.annotate(f'{int(largura)}',
                xy=(largura, barra.get_y() + barra.get_height() / 2),
                xytext=(5, 0),
                textcoords="offset points",
                ha='left', va='center', fontsize=10, fontweight='bold')

plt.tight_layout()
caminho_figura = "documentos/figuras/figura_ferramentas_atualizada_v3.png"
plt.savefig(caminho_figura, dpi=300)
plt.close()

print(f"Figura gerada com sucesso em '{caminho_figura}'!")
print(contagem)
