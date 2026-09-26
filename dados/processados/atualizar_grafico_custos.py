import matplotlib.pyplot as plt
import pandas as pd

# Dados consolidados reais extraídos de S001 a S011
data = {
    'Categoria_Custos': [
        'Treinamento e Capacitação / Desconhecimento',
        'Recursos Humanos / Carga Burocrática',
        'Infraestrutura e Recursos Insuficientes',
        'Privacidade, Confidencialidade e Dados Sensíveis'
    ],
    'Frequencia': [3, 6, 4, 5]
}

df = pd.DataFrame(data)
df = df.sort_values(by='Frequencia', ascending=True)

# Configuração da figura
plt.figure(figsize=(10, 6))
bars = plt.barh(df['Categoria_Custos'], df['Frequencia'], color='#b27008', edgecolor='none')

# Adicionar os valores numéricos nas barras
for bar in bars:
    width = bar.get_width()
    plt.text(width + 0.15, bar.get_y() + bar.get_height()/2, f'{int(width)}', 
             va='center', ha='left', fontsize=10, fontweight='bold', color='#333333')

# Estilização do gráfico
plt.xlabel('Frequência Absoluta (Número de Estudos)', fontsize=11, fontweight='bold', labelpad=10)
plt.ylabel('Categoria de Custos / Barreiras', fontsize=11, fontweight='bold', labelpad=10)
plt.title('Dimensões de Custos e Barreiras Relacionadas à GDI', fontsize=13, fontweight='bold', pad=15)

# Ajuste dos eixos e grelha
plt.xlim(0, 7)
plt.xticks([0, 1, 2, 3, 4, 5, 6, 7])
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Salvando a imagem na pasta correta do repositório
plt.tight_layout()
plt.savefig('documentos/figuras/figura_resultado_custos_tese.png', dpi=300)
print("Gráfico de custos atualizado com sucesso em documentos/figuras/figura_resultado_custos_tese.png!")