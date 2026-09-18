# Tese de Doutorado - PPGICS / Fiocruz

Repositório estruturado de documentação, dados e rotinas computacionais da pesquisa de doutorado em Informação e Comunicação em Saúde (PPGICS/ICICT/Fiocruz).

---

## Estrutura do Repositório

```text
Doutorado/
├── dados/
│   ├── brutos/                 # Arquivos brutos protegidos por versionamento
│   └── processados/
│       └── extracao_estudos.csv  # Planilha com os 30 campos de extração (JBI/MFDados)
├── documentos/
│   ├── figuras/                # Diagramas de fluxo e esquemas conceituais
│   └── protocolos/
│       ├── pgd.md              # Síntese do Plano de Gestão de Dados
│       ├── pgd_fiodmp.pdf      # PGD institucional exportado da plataforma FioDMP
│       ├── protocolo_revisao.md # Protocolo de revisão de escopo (JBI / PRISMA-ScR)
│       └── dicionario_dados_extracao.md # Codebook dos 30 campos de extração
├── scripts/
│   └── 01_valida_extracao.py   # Script em Python para auditoria e integridade do CSV
├── .gitignore                  # Regras de exclusão de dados volumosos/sensíveis
└── README.md                   # Apresentação geral do repositório