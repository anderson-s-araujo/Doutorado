import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import os

caminho_csv = "dados/processados/extracao_estudos.csv"
df = pd.read_csv(caminho_csv)

# Função de mapeamento para transformar texto livre em categorias limpas
def categoriza_ferramenta(texto):
    if not isinstance(texto, str):
        return "Não explicitado"
    t = texto.lower()
    if "dmponline" in t:
        return "DMPOnline"
    elif "moodle" in t:
        return "Moodle"
    elif "repository" in t or "repositório" in t or "frdr" in t or "kisti" in t:
        return "Repositório Institucional / Nacional"
    elif "explicitado" in t:
        return "Não explicitado"
    else:
        return "Outras Plataformas / Genérico"

# Aplicar a categorização
df["ferramenta_categoria"] = df["tools_or_platforms_mentioned"].apply(categoriza_ferramenta)

# Guardar a coluna categorizada no CSV
df.to_csv(caminho_csv, index=False, encoding="utf-8")

# Gerar o gráfico com as categorias limpas e frequências absolutas reais
contagem = df["ferramenta_categoria"].value_counts()

os.makedirs("documentos/figuras", exist_ok=True)
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')

fig, ax = plt.subplots(figsize=(10, 5))
barras = ax.barh(contagem.index, contagem.values, color="#1b4f72")

ax.xaxis.set_major_locator(ticker.MaxNIntegerLocator(integer=True))
ax.set_title("Distribuição Consolidada de Ferramentas e Plataformas (S001-S011)", fontsize=12, fontweight="bold")
ax.set_xlabel("Número de Estudos (Frequência Absoluta)", fontsize=10)
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
plt.savefig("documentos/figuras/figura1_ferramentas_reais.png", dpi=300)
plt.close()

print("Sucesso! Dados normalizados e gráfico analítico gerado com categorias limpas.")
print(contagem)
