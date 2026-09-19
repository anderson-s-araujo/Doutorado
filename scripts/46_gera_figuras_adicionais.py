import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("documentos/figuras", exist_ok=True)
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')

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

# 6. Cobertura Geográfica / Países
gera_grafico(
    ["Brasil", "Portugal", "Reino Unido", "Canadá", "Espanha"],
    [4, 3, 2, 1, 1],
    "Distribuição Geográfica dos Estudos (S001-S011)",
    "País de Origem",
    "#2471a3",
    "figura_resultado_paises_tese.png"
)

# 7. Alinhamento aos Princípios FAIR
gera_grafico(
    ["Encontrável (Findable)", "Acessível (Accessible)", "Interoperável (Interoperable)", "Reutilizável (Reusable)"],
    [5, 5, 3, 4],
    "Enfoque nos Princípios FAIR na Literatura Analisada",
    "Dimensão FAIR",
    "#884ea0",
    "figura_resultado_fair_tese.png"
)

print("Figuras analíticas adicionais (Países e FAIR) geradas com sucesso!")
