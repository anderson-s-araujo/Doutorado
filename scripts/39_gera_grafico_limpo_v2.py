uv run --with pandas --with matplotlib python scripts/39_gera_grafico_limpo_v2.pyimport pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import os

caminho_csv = "dados/processados/extracao_estudos.csv"
if not os.path.exists(caminho_csv):
    print("Erro: CSV não encontrado!")
    exit()

df = pd.read_csv(caminho_csv)

# Garantir que a coluna existe
coluna = "ferramenta_categoria" if "ferramenta_categoria" in df.columns else "tools_or_platforms_mentioned"
contagem = df[coluna].value_counts()

# Criar pasta e configurar estilo
os.makedirs("documentos/figuras", exist_ok=True)
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')

fig, ax = plt.subplots(figsize=(10, 5))
barras = ax.barh(contagem.index, contagem.values, color="#1b4f72")

# Forçar eixo X a usar apenas inteiros absolutos
ax.xaxis.set_major_locator(ticker.MaxNIntegerLocator(integer=True))
ax.set_title("Distribuição Absoluta de Ferramentas e Plataformas (S001-S011)", fontsize=12, fontweight="bold")
ax.set_xlabel("Frequência Absoluta (Número de Estudos)", fontsize=10)
ax.set_ylabel("Categoria / Ferramenta", fontsize=10)
ax.invert_yaxis()

# Adicionar os valores numéricos exatos no topo de cada barra
for barra in barras:
    largura = barra.get_width()
    ax.annotate(f'{int(largura)}',
                xy=(largura, barra.get_y() + barra.get_height() / 2),
                xytext=(5, 0),
                textcoords="offset points",
                ha='left', va='center', fontsize=10, fontweight='bold')

plt.tight_layout()

# Nome de ficheiro novo para evitar cache
caminho_figura = "documentos/figuras/figura_ferramentas_atualizada_v2.png"
plt.savefig(caminho_figura, dpi=300)
plt.close()

print(f"Novo gráfico gerado com sucesso em '{caminho_figura}'!")
print(contagem)
