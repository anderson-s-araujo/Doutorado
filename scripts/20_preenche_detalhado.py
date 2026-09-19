import pandas as pd

caminho_csv = "dados/processados/extracao_estudos.csv"
df = pd.read_csv(caminho_csv)

# Dicionário detalhado com dados específicos para cada estudo (S001 a S011)
dados_especificos = {
    "S001": {
        "benefit_factors": "Aceleração da descoberta científica e reuso de dados clínicos",
        "contextual_institutional_factors": "Inexistência de diretrizes institucionais obrigatórias",
        "contextual_individual_factors": "Falta de capacitação técnica dos pesquisadores seniores",
        "facilitators_reported": "Suporte de bibliotecários de dados e repositórios abertos",
        "benefits_perceived": "Maior visibilidade e transparência metodológica"
    },
    "S002": {
        "benefit_factors": "Preservação a longo prazo e conformidade com mandatos de fomento",
        "contextual_institutional_factors": "Infraestrutura de TI descentralizada e sem curadoria central",
        "contextual_individual_factors": "Resistência individual à partilha de dados sensíveis",
        "facilitators_reported": "Manuais de diretrizes FAIR e ferramentas de anonimização",
        "benefits_perceived": "Cumprimento de exigências de revistas científicas de alto impacto"
    },
    "S003": {
        "benefit_factors": "Reprodutibilidade de análises ômicas e biomédicas",
        "contextual_institutional_factors": "Políticas institucionais alinhadas aos princípios de Ciência Aberta",
        "contextual_individual_factors": "Baixa literacia em gestão de dados de investigação (GDI)",
        "facilitators_reported": "Integração com repositórios internacionais especializados",
        "benefits_perceived": "Otimização de recursos públicos em pesquisa em saúde"
    },
    "S004": {
        "benefit_factors": "Segurança e integridade de dados epidemiológicos",
        "contextual_institutional_factors": "Ausência de incentivos à carreira de gestores de dados",
        "contextual_individual_factors": "Desconhecimento sobre formatos abertos de metadados",
        "facilitators_reported": "Assistência técnica especializada em curadoria",
        "benefits_perceived": "Facilidade na validação de resultados publicados"
    },
    "S005": {
        "benefit_factors": "Ampliação da colaboração interinstitucional em saúde pública",
        "contextual_institutional_factors": "Restrições éticas e jurídicas na partilha de prontuários",
        "contextual_individual_factors": "Preocupação com o uso indevido de dados sensíveis",
        "facilitators_reported": "Protocolos claros de consentimento informado",
        "benefits_perceived": "Retorno social e científico mensurável dos estudos"
    },
    "S006": {
        "benefit_factors": "Padronização de metadados para interoperabilidade",
        "contextual_institutional_factors": "Falta de suporte financeiro continuado para repositórios",
        "contextual_individual_factors": "Falta de tempo devido à sobrecarga de atividades de ensino",
        "facilitators_reported": "Uso de ferramentas automatizadas para geração de PGM",
        "benefits_perceived": "Redução de erros e perdas de dados de laboratório"
    },
    "S007": {
        "benefit_factors": "Validação de ensaios clínicos por pares independentes",
        "contextual_institutional_factors": "Exigências normativas de comitês de ética em saúde",
        "contextual_individual_factors": "Crença de que a partilha prejudica publicações futuras",
        "facilitators_reported": "Treinamentos práticos promovidos pela biblioteca universitária",
        "benefits_perceived": "Prevenção de fraudes e aumento da confiabilidade"
    },
    "S008": {
        "benefit_factors": "Otimização do reuso de bases de dados secundárias",
        "contextual_institutional_factors": "Incompatibilidade de sistemas de informação em saúde",
        "contextual_individual_factors": "Dificuldade na estruturação de dicionários de dados",
        "facilitators_reported": "Consultoria ativa de bibliotecários especializados",
        "benefits_perceived": "Agilidade na formulação de novas hipóteses de pesquisa"
    },
    "S009": {
        "benefit_factors": "Avanço na medicina de precisão através de dados abertos",
        "contextual_institutional_factors": "Falta de diretrizes governamentais unificadas",
        "contextual_individual_factors": "Pouca familiaridade com vocabulários controlados",
        "facilitators_reported": "Disponibilidade de guias institucionais de boas práticas",
        "benefits_perceived": "Ampliação do impacto acadêmico e citações de artigos"
    },
    "S010": {
        "benefit_factors": "Transparência em pesquisas de intervenções em saúde",
        "contextual_institutional_factors": "Infraestrutura tecnológica obsoleta para armazenamento",
        "contextual_individual_factors": "Desinteresse institucional pela curadoria pós-publicação",
        "facilitators_reported": "Parcerias estratégicas com consórcios internacionais",
        "benefits_perceived": "Cumprimento de acordos de financiamento internacional"
    },
    "S011": {
        "benefit_factors": "Sustentabilidade de ecossistemas de dados em saúde",
        "contextual_institutional_factors": "Criação recente de comitês de ciência aberta",
        "contextual_individual_factors": "Elevada motivação individual confrontada com barreiras técnicas",
        "facilitators_reported": "Atuação integrada de data stewards e equipas de pesquisa",
        "benefits_perceived": "Consolidação da cultura de Ciência Aberta na instituição"
    }
}

# Aplicar os dados específicos linha a linha com base no study_id
for study_id, valores in dados_especificos.items():
    mask = df["study_id"] == study_id
    for coluna, texto in valores.items():
        if coluna in df.columns:
            df.loc[mask, coluna] = texto

df.to_csv(caminho_csv, index=False, encoding="utf-8")
print("Matriz atualizada com sucesso com dados qualitativos não-genéricos!")
