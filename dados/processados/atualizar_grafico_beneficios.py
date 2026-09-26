import matplotlib.pyplot as plt
import pandas as pd

# Dados consolidados dos benefícios (S001 a S011)
data = {
    'Categoria_Beneficios': [
        'Preservação a Longo Prazo',
        'Colaboração Científica',
        'Conformidade com Princípios FAIR',
        'Reutilização e Acesso Aberto'
    ],
    'Frequencia': [3, 3, 4, 5]
}

df = pd.DataFrame(data)

# Configuração da figura
plt.figure(figsize=(10, 6))
bars = plt.barh(df['Categoria_Beneficios'], df['Frequencia'], color='#2ca25f', edgecolor='none')

# Adicionar os valores numéricos nas barras
for bar in bars:
    width = bar.get_width()
    plt.text(width + 0.15, bar.get_y() + bar.get_height()/2, f'{int(width)}', 
             va='center', ha='left', fontsize=10, fontweight='bold', color='#333333')

# Estilização do gráfico
plt.xlabel('Frequência Absoluta (Número de Estudos)', fontsize=11, fontweight='bold', labelpad=10)
plt.ylabel('Categoria de Benefícios', fontsize=11, fontweight='bold', labelpad=10)
plt.title('Benefícios Relacionados à Gestão de Dados (MFDados)', fontsize=13, fontweight='bold', pad=15)

# Ajuste dos eixos e grelha
plt.xlim(0, 6)
plt.xticks([0, 1, 2, 3, 4, 5, 6])
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Salvando a imagem na pasta correta do repositório
plt.tight_layout()
plt.savefig('documentos/figuras/figura_resultado_beneficios_tese.png', dpi=300)
print("Gráfico de benefícios atualizado com sucesso!")