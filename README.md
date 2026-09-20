```text
Doutorado/
├── dados/
│   ├── brutos/                 # Arquivos brutos protegidos por versionamento
│   └── processados/
│       ├── cruzamento_atores_dmp.csv      # Mapeamento analítico de atores e DMP
│       ├── cruzamento_desenho_dmp.csv     # Mapeamento de delineamentos metodológicos
│       └── extracao_estudos.csv           # Planilha com os 30 campos de extração (JBI/MFDados)
├── documentos/
│   ├── figuras/                # Diagramas, fluxos e figuras analíticas (dpi=300)
│   └── protocolos/
│       ├── dicionario_dados_extracao.md   # Codebook dos 30 campos de extração
│       ├── pgd_fiodmp.pdf                 # PGD institucional exportado da plataforma FioDMP
│       ├── pgd.md                         # Síntese do Plano de Gestão de Dados
│       ├── protocolo_revisao.md           # Protocolo de revisão de escopo (JBI / PRISMA-ScR)
│       └── tabelas_resultados_tese.md     # Tabelas consolidadas para a tese
├── scripts/
│   ├── 01_valida_extracao.py              # Script em Python para auditoria e integridade do CSV
│   ├── 02_estatisticas_descritivas.py     # Script para análises descritivas do corpus
│   ├── 03_popula_extracao.py              # Automação de povoamento de dados
│   ├── 05_analise_frequencias.py          # Cálculo de frequências absolutas
│   └── 46_gera_figuras_adicionais.py      # Renderização de gráficos complementares
├── .gitignore                  # Regras de exclusão de dados volumosos/sensíveis
└── README.md                   # Apresentação geral do repositório
