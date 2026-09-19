import pandas as pd
import matplotlib.pyplot as plt
import os

caminho_csv = "dados/processados/extracao_estudos.csv"
if not os.path.exists(caminho_csv):
    print("Ficheiro CSV não encontrado!")
    exit()

df = pd.read_csv(caminho_csv)
os.makedirs("documentos/figuras", exist_ok=True)
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')

coluna_alvo = "tools_or_platforms_mentioned"
if coluna_alvo in df.columns:
    # Conta a frequência real de cada termo único na coluna
    contagem = df[coluna_alvo].value_counts()
    
    plt.figure(figsize=(10, 5))
    contagem.plot(kind="barh", color="#1f4e78")
    plt.title("Distribuição Real de Ferramentas e Plataformas (S001-S011)", fontsize=12, fontweight="bold")
    plt.xlabel("Número de Ocorrências (Estudos)", fontsize=10)
    plt.ylabel("Ferramenta / Contexto", fontsize=10)
    plt.gca().invert_yaxis()
    plt.tight_layout()
    
    caminho_figura = "documentos/figuras/figura1_ferramentas_reais.png"
    plt.savefig(caminho_figura, dpi=300)
    plt.close()
    print(f"Gráfico real gerado com sucesso em '{caminho_figura}'!")
    print(contagem)
else:
    print(f"Coluna '{coluna_alvo}' não encontrada no DataFrame.")
