import matplotlib.pyplot as plt
import pandas as pd

# Dados consolidados reais da distribuição geográfica (S001 a S011)
data = {
    'Pais_Origem': [
        'Finlândia, Suécia e Malawi',
        'Canadá',
        'Iraque',
        'Índia',
        'Turquia',
        'África do Sul',
        'Estados Unidos'
    ],
    'Frequencia': [1, 1, 1, 1, 1, 1, 5]
}

df = pd.DataFrame(data)

# Configuração da figura
plt.figure(figsize=(10, 6))
bars = plt.barh(df['Pais_Origem'], df['Frequencia'], color='#1f618d', edgecolor='none')

# Adicionar os valores numéricos nas barras
for bar in bars:
    width = bar.get_width()
    plt.text(width + 0.15, bar.get_y() + bar.get_height()/2, f'{int(width)}', 
             va='center', ha='left', fontsize=10, fontweight='bold', color='#333333')

# Estilização do gráfico
plt.xlabel('Frequência Absoluta (Número de Estudos)', fontsize=11, fontweight='bold', labelpad=10)
plt.ylabel('País de Origem / Região', fontsize=11, fontweight='bold', labelpad=10)
plt.title('Distribuição Geográfica dos Estudos (S001-S011)', fontsize=13, fontweight='bold', pad=15)

# Ajuste dos eixos e grelha
plt.xlim(0, 6)
plt.xticks([0, 1, 2, 3, 4, 5, 6])
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Salvando a imagem na pasta correta do repositório
plt.tight_layout()
plt.savefig('documentos/figuras/figura_resultado_paises_tese.png', dpi=300)
print("Gráfico de países atualizado com sucesso em documentos/figuras/figura_resultado_paises_tese.png!")