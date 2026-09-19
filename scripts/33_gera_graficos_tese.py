import pandas as pd
import matplotlib.pyplot as plt
import os

caminho_csv = "dados/processados/extracao_estudos.csv"
df = pd.read_csv(caminho_csv)

os.makedirs("documentos/figuras", exist_ok=True)
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')

# 1. Gráfico de Frequência de Ferramentas / Plataformas Mencionadas
if "tools_or_platforms_mentioned" in df.columns:
    plt.figure(figsize=(10, 5))
    contagem_ferramentas = df["tools_or_platforms_mentioned"].value_counts().head(5)
    contagem_ferramentas.plot(kind="barh", color="#2b5c8f")
    plt.title("Plataformas e Ferramentas Mais Citadas nos Estudos (S001-S011)", fontsize=11, fontweight="bold")
    plt.xlabel("Frequência de Menção", fontsize=10)
    plt.ylabel("Ferramenta / Plataforma", fontsize=10)
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig("documentos/figuras/grafico_ferramentas_real.png", dpi=300)
    plt.close()

# 2. Gráfico de Distribuição por País / Região Real
if "country_region" in df.columns:
    plt.figure(figsize=(9, 5))
    contagem_paises = df["country_region"].value_counts()
    contagem_paises.plot(kind="bar", color="#d95f02")
    plt.title("Distribuição Geográfica dos Estudos Analisados", fontsize=11, fontweight="bold")
    plt.xlabel("País / Região", fontsize=10)
    plt.ylabel("Número de Estudos", fontsize=10)
    plt.xticks(rotation=25, ha="right")
    plt.tight_layout()
    plt.savefig("documentos/figuras/grafico_paises_real.png", dpi=300)
    plt.close()

print("Gráficos analíticos reais gerados com sucesso na pasta 'documentos/figuras/'!")
