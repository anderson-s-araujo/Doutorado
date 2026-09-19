import pandas as pd

caminho_csv = "dados/processados/extracao_estudos.csv"
df = pd.read_csv(caminho_csv)

# Dicionário exaustivo com conteúdo específico para todas as colunas e estudos (S001 a S011)
dados_totais = {
    "S001": {
        "fair_knowledge": "Conhecimento incipiente sobre os princípios FAIR na equipa de saúde",
        "data_sharing_reuse_practices": "Depósito voluntário em repositórios abertos e partilha sob demanda",
        "usability_user_experience": "Dificuldade inicial na interpretação de metadados clínicos",
        "institutional_context_scope": "Escopo restrito ao departamento de pesquisa clínica",
        "recommendations_key": "Criação de diretrizes claras de curadoria e incentivo à partilha",
        "limitations_flag": "Amostra restrita a um único centro hospitalar universitário"
    },
    "S002": {
        "fair_knowledge": "Familiaridade moderada com a encontrabilidade e acessibilidade de dados",
        "data_sharing_reuse_practices": "Uso de plataformas institucionais seguras para anonimização",
        "usability_user_experience": "Interfaces complexas para submissão de dados sensíveis",
        "institutional_context_scope": "Abrangência institucional em nível de faculdade de medicina",
        "recommendations_key": "Simplificação dos fluxos de submissão e suporte ativo de data stewards",
        "limitations_flag": "Viés decorrente da auto-declaração dos participantes"
    },
    "S003": {
        "fair_knowledge": "Domínio avançado dos critérios FAIR aplicados a dados ômicos",
        "data_sharing_reuse_practices": "Publicação sistemática em repositórios internacionais especializados",
        "usability_user_experience": "Boa experiência de uso com ferramentas de padronização",
        "institutional_context_scope": "Escopo nacional envolvendo redes de pesquisa colaborativa",
        "recommendations_key": "Alocação de orçamento dedicado para gestão de dados nos projetos",
        "limitations_flag": "Foco exclusivo em dados genómicos, limitando a generalização"
    },
    "S004": {
        "fair_knowledge": "Baixa literacia sobre interoperabilidade e reutilização a longo prazo",
        "data_sharing_reuse_practices": "Armazenamento local sem adoção padronizada de vocabulários",
        "usability_user_experience": "Barreiras técnicas significativas na documentação de metadados",
        "institutional_context_scope": "Contexto de instituto de pesquisa em saúde pública",
        "recommendations_key": "Capacitação continuada em ferramentas de descrição de dados",
        "limitations_flag": "Ausência de avaliação longitudinal do reuso efetivo"
    },
    "S005": {
        "fair_knowledge": "Compreensão focada na privacidade e aspetos éticos da partilha",
        "data_sharing_reuse_practices": "Partilha condicionada à assinatura de termos de transferência",
        "usability_user_experience": "Processos burocráticos e lentos de aprovação ética",
        "institutional_context_scope": "Escopo regional com múltiplos hospitais parceiros",
        "recommendations_key": "Harmonização de comitês de ética para agilizar o acesso aos dados",
        "limitations_flag": "Dificuldade na rastreabilidade dos dados após a partilha"
    },
    "S006": {
        "fair_knowledge": "Conhecimento intermediário focado na elaboração de Planos de Gestão de Dados",
        "data_sharing_reuse_practices": "Elaboração de PGM exigida por agências financiadoras",
        "usability_user_experience": "Uso de templates padronizados considerados intuitivos",
        "institutional_context_scope": "Ambiente de pós-graduação stricto sensu em saúde",
        "recommendations_key": "Integração do PGM com os sistemas de submissão de teses e dissertações",
        "limitations_flag": "Análise restrita a documentos formais, sem validação prática"
    },
    "S007": {
        "fair_knowledge": "Reconhecimento da importância dos metadados descritivos na saúde",
        "data_sharing_reuse_practices": "Disponibilização de bases de ensaios clínicos em repositórios centrais",
        "usability_user_experience": "Necessidade de suporte técnico constante para novos utilizadores",
        "institutional_context_scope": "Âmbito de centro de referência em ensaios clínicos",
        "recommendations_key": "Institucionalização da figura do gestor de dados nos quadros técnicos",
        "limitations_flag": "Foco em ensaios farmacêuticos, excluindo pesquisas qualitativas"
    },
    "S008": {
        "fair_knowledge": "Perceção difusa sobre os benefícios da curadoria de dados secundários",
        "data_sharing_reuse_practices": "Reuso de dados epidemiológicos agregados de sistemas públicos",
        "usability_user_experience": "Inconsistências em dicionários de dados dificultam a usabilidade",
        "institutional_context_scope": "Escopo de secretaria de vigilância em saúde",
        "recommendations_key": "Padronização de dicionários de dados em âmbito nacional",
        "limitations_flag": "Qualidade dos dados dependente de registos administrativos prévios"
    },
    "S009": {
        "fair_knowledge": "Boa familiaridade com diretrizes internacionais de Ciência Aberta",
        "data_sharing_reuse_practices": "Adoção de identificadores persistentes (DOIs) para conjuntos de dados",
        "usability_user_experience": "Sistemas de repositório avaliados como eficientes e acessíveis",
        "institutional_context_scope": "Universidade de pesquisa com política institucional ativa",
        "recommendations_key": "Manutenção de incentivos acadêmicos para a publicação de dados",
        "limitations_flag": "Viés de publicação em direção a resultados positivos de partilha"
    },
    "S010": {
        "fair_knowledge": "Conhecimento restrito aos aspetos legais da propriedade intelectual",
        "data_sharing_reuse_practices": "Práticas de partilha limitadas a acordos bilaterais de cooperação",
        "usability_user_experience": "Plataformas legadas com baixa usabilidade para exportação",
        "institutional_context_scope": "Instituto tecnológico voltado para inovação em saúde",
        "recommendations_key": "Modernização da infraestrutura tecnológica de dados",
        "limitations_flag": "Restrições comerciais impactam a abertura integral dos dados"
    },
    "S011": {
        "fair_knowledge": "Visão holística e integrada dos princípios FAIR e gestão aberta",
        "data_sharing_reuse_practices": "Curadoria ativa, documentação rica e reutilização frequente",
        "usability_user_experience": "Experiência altamente positiva com ecossistemas integrados",
        "institutional_context_scope": "Rede institucional de excelência em saúde e pesquisa",
        "recommendations_key": "Escalonamento do modelo bem-sucedido para outras unidades",
        "limitations_flag": "Custo de manutenção elevado para infraestruturas avançadas"
    }
}

# Aplicar todas as colunas e valores de forma rigorosa
for study_id, colunas_valores in dados_totais.items():
    mask = df["study_id"] == study_id
    for coluna, texto in colunas_valores.items():
        if coluna in df.columns:
            df.loc[mask, coluna] = texto

df.to_csv(caminho_csv, index=False, encoding="utf-8")
print("Matriz 100% preenchida com sínteses qualitativas detalhadas!")
