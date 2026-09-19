import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("documentos/figuras", exist_ok=True)
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')

# Função auxiliar para gerar gráficos de barras horizontais padronizados
def gera_grafico(categorias, frequencias, titulo, ylabel, cor, nome_ficheiro):
    plt.figure(figsize=(9, 5))
    barras = plt.barh(categorias, frequencias, color=cor, height=0.55)
    plt.title(titulo, fontsize=11, fontweight="bold")
    plt.xlabel("Frequência Absoluta (Número de Estudos)", fontsize=10)
    plt.ylabel(ylabel, fontsize=10)
    plt.gca().invert_yaxis()

    for barra in barras:
        largura = barra.get_width()
        plt.text(largura + 0.1, barra.get_y() + barra.get_height()/2, f'{int(largura)}', 
                 va='center', ha='left', fontsize=10, fontweight='bold')

    plt.xlim(0, max(frequencias) + 1.5)
    plt.tight_layout()
    plt.savefig(f"documentos/figuras/{nome_ficheiro}", dpi=300)
    plt.close()

# 1. Ferramentas e Plataformas de PGD
gera_grafico(
    ["DMPOnline", "Repositório Institucional", "Repositório Nacional", "Moodle", "Não explicitado"],
    [4, 3, 2, 1, 1],
    "Plataformas e Ferramentas de PGD Mencionadas (S001-S011)",
    "Categoria / Ferramenta",
    "#1b4f72",
    "figura_resultado_ferramentas_tese.png"
)

# 2. Delineamento Metodológico
gera_grafico(
    ["Revisão Sistemática", "Estudo de Caso", "Pesquisa Documental", "Ensaio Metodológico"],
    [5, 3, 2, 1],
    "Distribuição por Delineamento Metodológico (S001-S011)",
    "Delineamento",
    "#117a65",
    "figura_resultado_delineamentos_tese.png"
)

# 3. Fatores Relacionados (MFDados)
gera_grafico(
    ["Organizacionais", "Tecnológicos", "Legais / Conformidade", "Financeiros"],
    [5, 4, 3, 2],
    "Fatores Relacionados Identificados (MFDados)",
    "Categoria de Fatores",
    "#7d3c98",
    "figura_resultado_fatores_tese.png"
)

# 4. Custos Relacionados
gera_grafico(
    ["Infraestrutura e Armazenamento", "Recursos Humanos / Curadoria", "Treinamento e Capacitação", "Não explicitado"],
    [4, 4, 2, 1],
    "Dimensões de Custos Relacionadas à GDI",
    "Categoria de Custos",
    "#b9770e",
    "figura_resultado_custos_tese.png"
)

# 5. Benefícios Relacionados
gera_grafico(
    ["Reutilização e Acesso Aberto", "Conformidade com Princípios FAIR", "Preservação a Longo Prazo", "Colaboração Científica"],
    [5, 4, 3, 3],
    "Benefícios Relacionados à Gestão de Dados (MFDados)",
    "Categoria de Benefícios",
    "#28b463",
    "figura_resultado_beneficios_tese.png"
)

print("Todas as 5 figuras analíticas definitivas da tese foram geradas com sucesso!")
