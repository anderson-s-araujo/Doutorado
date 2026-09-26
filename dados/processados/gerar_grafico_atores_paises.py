import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Dados consolidados do cruzamento entre Atores de Apoio e Regiões/Países
paises = ['Brasil', 'Portugal', 'Reino Unido', 'Canadá', 'Outros (Finlândia, África, etc.)']
atores_financiadores = [2, 1, 1, 0, 1]
atores_bibliotecarios = [1, 2, 1, 1, 2]
atores_data_stewards = [1, 1, 2, 0, 1]

x = np.arange(len(paises))
width = 0.25

# Configuração da figura
plt.figure(figsize=(11, 6))

# Construção das barras agrupadas
plt.bar(x - width, atores_financiadores, width, label='Agências de Financiamento', color='#1b4f72')
plt.bar(x, atores_bibliotecarios, width, label='Bibliotecários / Data Stewards', color='#28b463')
plt.bar(x + width, atores_data_stewards, width, label='Gestores Institucionais / Outros', color='#7d3c98')

# Estilização do gráfico
plt.xlabel('País / Região Geográfica', fontsize=11, fontweight='bold', labelpad=10)
plt.ylabel('Frequência de Menção nos Estudos', fontsize=11, fontweight='bold', labelpad=10)
plt.title('Cruzamento de Atores de Apoio por Região Geográfica (S001-S011)', fontsize=13, fontweight='bold', pad=15)
plt.xticks(x, paises, fontsize=10)
plt.legend(frameon=True, facecolor='white', edgecolor='none')

plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Salvando a imagem na pasta de figuras do repositório
plt.tight_layout()
plt.savefig('documentos/figuras/figura_resultado_atores_paises.png', dpi=300)
print("Gráfico de atores e países gerado e guardado com sucesso em documentos/figuras/figura_resultado_atores_paises.png!")