import matplotlib.pyplot as plt
import pandas as pd

# Dados reais consolidados dos delineamentos metodológicos (S001 a S011)
data = {
    'Delineamento': [
        'Outro / Aplicação Técnica',
        'Entrevista',
        'Relato de Experiência',
        'Estudo de Caso / Métodos Mistos',
        'Survey (Inquérito)'
    ],
    'Frequencia': [1, 1, 2, 3, 4]
}

df = pd.DataFrame(data)

# Configuração da figura
plt.figure(figsize=(10, 6))
bars = plt.barh(df['Delineamento'], df['Frequencia'], color='#005a32', edgecolor='none')

# Adicionar os valores numéricos nas barras
for bar in bars:
    width = bar.get_width()
    plt.text(width + 0.15, bar.get_y() + bar.get_height()/2, f'{int(width)}', 
             va='center', ha='left', fontsize=10, fontweight='bold', color='#333333')

# Estilização do gráfico
plt.xlabel('Frequência Absoluta (Número de Estudos)', fontsize=11, fontweight='bold', labelpad=10)
plt.ylabel('Delineamento Metodológico', fontsize=11, fontweight='bold', labelpad=10)
plt.title('Distribuição por Delineamento Metodológico (S001-S011)', fontsize=13, fontweight='bold', pad=15)

# Ajuste dos eixos e grelha
plt.xlim(0, 5)
plt.xticks([0, 1, 2, 3, 4, 5])
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Salvando a imagem na pasta correta do repositório
plt.tight_layout()
plt.savefig('documentos/figuras/figura_resultado_delineamento_tese.png', dpi=300)
print("Gráfico de delineamento atualizado com sucesso em documentos/figuras/figura_resultado_delineamento_tese.png!")