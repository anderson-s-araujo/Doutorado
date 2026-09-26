import matplotlib.pyplot as plt
import pandas as pd

# Dados consolidados dos estudos (S001 a S011)
data = {
    'Delineamento': [
        'Estudo transversal quantitativo',
        'Pesquisa qualitativa exploratória',
        'Estudo metodológico computacional',
        'Investigação descritiva observacional',
        'Estudo de caso qualitativo',
        'Pesquisa survey com análise estatística',
        'Revisão sistemática com análise documental',
        'Estudo analítico de bases secundárias',
        'Estudo bibliométrico e cienciométrico',
        'Análise de inovação tecnológica',
        'Pesquisa-ação participativa'
    ],
    'Frequencia': [4, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2]
}

df = pd.DataFrame(data)
df = df.sort_values(by='Frequencia', ascending=True)

# Configuração da figura
plt.figure(figsize=(10, 6))
bars = plt.barh(df['Delineamento'], df['Frequencia'], color='#1b7837', edgecolor='none')

# Estilização do gráfico
plt.xlabel('Número de Estudos', fontsize=11, fontweight='bold', labelpad=10)
plt.ylabel('Delineamento Metodológico', fontsize=11, fontweight='bold', labelpad=10)
plt.title('Distribuição dos Delineamentos Metodológicos Reais', fontsize=13, fontweight='bold', pad=15)

# Ajuste dos eixos e grelha
plt.xlim(0, 5)
plt.xticks([0, 1, 2, 3, 4, 5])
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Salvando a imagem na pasta correta do repositório
plt.tight_layout()
plt.savefig('documentos/figuras/figura2_delineamentos_reais.png', dpi=300)
print("Gráfico atualizado e guardado com sucesso em documentos/figuras/figura2_delineamentos_reais.png!")