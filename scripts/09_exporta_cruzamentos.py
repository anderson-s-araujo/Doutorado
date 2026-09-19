import os
import pandas as pd

# Garantir que a pasta de resultados existe
pasta_resultados = "dados/processados/resultados"
os.makedirs(pasta_resultados, exist_ok=True)

# Carregar a base de dados processada
caminho_csv = "dados/processados/extracao_estudos.csv"
df = pd.read_csv(caminho_csv)

# 1. Gerar tabela cruzada: Desenho de Estudo vs Requisitos de PDM
cruzamento_1 = pd.crosstab(df["study_design"], df["dmp_context_and_requirement"], margins=True)
caminho_tabela_1 = os.path.join(pasta_resultados, "cruzamento_desenho_dmp.csv")
cruzamento_1.to_csv(caminho_tabela_1, encoding="utf-8")

# 2. Gerar tabela cruzada: Atores de Suporte vs Requisitos de PDM
cruzamento_2 = pd.crosstab(df["support_actors_mentioned"], df["dmp_context_and_requirement"], margins=True)
caminho_tabela_2 = os.path.join(pasta_resultados, "cruzamento_atores_dmp.csv")
cruzamento_2.to_csv(caminho_tabela_2, encoding="utf-8")

print(f"Tabelas de cruzamento exportadas com sucesso para a pasta: {pasta_resultados}")
