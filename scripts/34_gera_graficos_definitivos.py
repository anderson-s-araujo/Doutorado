import pandas as pd
import matplotlib.pyplot as plt
import os

caminho_csv = "dados/processados/extracao_estudos.csv"
df = pd.read_csv(caminho_csv)

# Garantir diretoria limpa
os.makedirs("documentos/figuras", exist_ok=True)
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')

# 1. Gráfico Analítico Real de Ferramentas / Plataformas
if "tools_or_platforms_mentioned" in df.columns:
    plt.figure(figsize=(10, 5))
    contagem = df["tools_or_platforms_mentioned"].value_counts().head(6)
    contagem.plot(kind="barh", color="#1b4f72")
    plt.title("Frequência de Plataformas e Repositórios nos Estudos (S001-S011)", fontsize=12, fontweight="bold")
    plt.xlabel("Número de Ocorrências", fontsize=10)
    plt.ylabel("Plataforma / Ferramenta", fontsize=10)
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig("documentos/figuras/figura1_ferramentas_reais.png", dpi=300)
    plt.close()

# 2. Gráfico Analítico Real de Delineamento dos Estudos
if "study_design" in df.columns:
    plt.figure(figsize=(10, 5))
    contagem_design = df["study_design"].value_counts()
    contagem_design.plot(kind="barh", color="#117a65")
    plt.title("Distribuição dos Delineamentos Metodológicos Reais", fontsize=12, fontweight="bold")
    plt.xlabel("Número de Estudos", fontsize=10)
    plt.ylabel("Delineamento", fontsize=10)
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig("documentos/figuras/figura2_delineamentos_reais.png", dpi=300)
    plt.close()

print("Novos gráficos analíticos gerados com sucesso!")
