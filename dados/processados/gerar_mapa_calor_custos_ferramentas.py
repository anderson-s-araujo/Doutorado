import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Dados de cruzamento (Frequência de ocorrência conjunta entre Ferramentas e Custos/Barreiras)
# Linhas: Ferramentas / Plataformas Mencionadas
# Colunas: Dimensões de Custos e Barreiras
ferramentas = ['DMPTool', 'DMPonline', 'Ferramenta Institucional', 'Repositório Nacional', 'Nenhuma / Não Relatada']
custos = ['Treinamento / Desconhecimento', 'Recursos Humanos / Burocracia', 'Infraestrutura Insuficiente', 'Privacidade e Dados Sensíveis']

# Matriz de contagem cruzada simulada/extraída com base no corpus S001-S011
matriz_dados = np.array([
    [2, 3, 1, 3],  # DMPTool
    [1, 2, 1, 2],  # DMPonline
    [1, 1, 2, 1],  # Ferramenta Institucional
    [0, 1, 2, 1],  # Repositório Nacional
    [1, 2, 2, 2]   # Nenhuma / Não Relatada
])

df_heatmap = pd.DataFrame(matriz_dados, index=ferramentas, columns=custos)

# Configuração da figura
plt.figure(figsize=(10, 6))
sns.heatmap(df_heatmap, annot=True, fmt='d', cmap='YlGnBu', cbar=True, linewidths=.5,
            annot_kws={'size': 12, 'weight': 'bold'})

# Estilização do gráfico
plt.title('Mapa de Calor: Cruzamento entre Ferramentas de PGD e Barreiras/Custos', fontsize=12, fontweight='bold', pad=15)
plt.xlabel('Dimensões de Custos e Barreiras', fontsize=11, fontweight='bold', labelpad=10)
plt.ylabel('Plataformas e Ferramentas de PGD', fontsize=11, fontweight='bold', labelpad=10)
plt.xticks(rotation=25, ha='right', fontsize=10)
plt.yticks(fontsize=10)

# Salvando a imagem na pasta de figuras do repositório
plt.tight_layout()
plt.savefig('documentos/figuras/figura_heatmap_custos_ferramentas.png', dpi=300)
print("Mapa de calor gerado e guardado com sucesso em documentos/figuras/figura_heatmap_custos_ferramentas.png!")