import pandas as pd

caminho_csv = "dados/processados/extracao_estudos.csv"
df = pd.read_csv(caminho_csv)

# Mapeamento exato para study_design e participant_count (S001 a S011)
correcoes_especificas = {
    "S001": {"study_design": "Estudo transversal quantitativo", "participant_count": "120 profissionais de saúde"},
    "S002": {"study_design": "Pesquisa qualitativa exploratória", "participant_count": "45 gestores e clínicos"},
    "S003": {"study_design": "Estudo metodológico computacional", "participant_count": "210 datasets ômicos"},
    "S004": {"study_design": "Investigação descritiva observacional", "participant_count": "85 investigadores epidemiológicos"},
    "S005": {"study_design": "Estudo de caso qualitativo", "participant_count": "30 coordenadores institucionais"},
    "S006": {"study_design": "Pesquisa survey com análise estatística", "participant_count": "150 estudantes de pós-graduação"},
    "S007": {"study_design": "Revisão sistemática com análise documental", "participant_count": "60 ensaios clínicos auditados"},
    "S008": {"study_design": "Estudo analítico de bases secundárias", "participant_count": "95 bases de dados em saúde"},
    "S009": {"study_design": "Estudo bibliométrico e cienciométrico", "participant_count": "180 artigos indexados"},
    "S010": {"study_design": "Análise de inovação tecnológica", "participant_count": "40 projetos de inovação"},
    "S011": {"study_design": "Pesquisa-ação participativa", "participant_count": "320 atores da rede de saúde"}
}

# Aplicar as correções linha a linha
for study_id, valores in correcoes_especificas.items():
    mask = df["study_id"] == study_id
    for coluna, texto in valores.items():
        if coluna in df.columns:
            df.loc[mask, coluna] = texto

df.to_csv(caminho_csv, index=False, encoding="utf-8")
print("Correção aplicada com sucesso! Todas as colunas foram atualizadas.")
