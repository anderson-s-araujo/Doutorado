# PROTOCOLO DE ESTUDO
## Percepções e práticas dos pesquisadores em relação aos Planos de Gestão de Dados e às ferramentas de PGD: protocolo de revisão de escopo

**Financiamento:** Conselho Nacional de Desenvolvimento Científico e Tecnológico (CNPq), Brasil.  
**Registro:** Open Science Framework (OSF) - [inserir link]  
**Depósito do PGD:** [Zenodo - Record 17727630](https://zenodo.org/records/17727630?preview_file=search_strategies_DMP_requirements.txt)  
**Data da última revisão:** Junho/Agosto de 2026  

---

### Autoria e Afiliações
* **Viviane Santos de Oliveira Veiga** (Fiocruz / Univ. Twente / Harvard Univ.)
* **Patrícia Henning** (UNIRIO)
* **Simone Dib** (Fiocruz)
* **Camila Belo** (Fiocruz / INCA)
* **Isabella Henrique Lima Pereira** (UFF)
* **Anderson Araújo** (Fiocruz)
* **Fábio Bernardo da Silva** (Fiocruz)
* **Julia Dias Mota** (Fiocruz)

---

## 1. Resumo e Objetivo
* **Introdução:** Os PGDs apoiam a organização, documentação, preservação e reuso de dados alinhados aos Princípios FAIR, mas persistem lacunas entre recomendações técnicas, exigências institucionais e a adesão prática dos pesquisadores.
* **Objetivo Geral:** Mapear e sintetizar evidências sobre como pesquisadores do campo da saúde percebem, utilizam e experienciam PGDs e ferramentas digitais de apoio ao longo do ciclo de vida da pesquisa, considerando práticas de elaboração, atualização, monitoramento e uso, além de fatores de custos, benefícios e contextos institucionais e individuais.
* **Referencial Teórico:** Modelo de Fatores que Influenciam no Comportamento de Compartilhamento de Dados de Pesquisa (**MFDados**), adaptado para análise de fatores de custos, benefícios e contextuais (institucionais e individuais).

---

## 2. Metodologia e Delineamento (JBI / PRISMA-ScR)
* **Metodologia:** Joanna Briggs Institute (JBI) para revisões de escopo e extensão PRISMA-ScR.
* **Pergunta de Revisão (Estratégia PCC):**
  * **P (População):** Pesquisadores do campo da saúde (docentes, pesquisadores e pós-graduandos *stricto sensu*).
  * **C (Conceito):** Percepções, práticas, experiências, fatores de custos, benefícios, contextuais (institucionais/individuais), usabilidade e adesão a PGDs e ferramentas.
  * **C (Contexto):** Universidades, centros de pesquisa, hospitais universitários e ambientes institucionais com ênfase em Ciência Aberta e Princípios FAIR.

### Estratégia de Busca e Fontes (Cobertura: 2014–2026)
* **PubMed/MEDLINE:** 332 registros
* **Scopus:** 926 registros
* **Web of Science (WoS):** 941 registros
* **BRAPCI:** 100 registros
* **LILACS:** 5 registros

---

## 3. Seleção dos Estudos e Gestão de Registros
1. **Deduplicação:** Mendeley Desktop.
2. **Triagem por pares independentes:** Plataforma Rayyan (fase 1: títulos/resumos; fase 2: leitura integral).
3. **Resolução de conflitos:** Consenso ou terceiro revisor.
4. **Relatório:** Fluxograma PRISMA-ScR.

---

## 4. Ficha de Extração de Dados (Campos Controlados)

| Campo | Descrição / Restrição | Observação / Formato |
| :--- | :--- | :--- |
| `study_id` | Identificador único atribuído na triagem | Ex.: S001 (Rayyan) |
| `citation` | Referência bibliográfica | Estilo Vancouver |
| `doi_or_url` | DOI ou identificador persistente | Priorizar DOI |
| `document_type` | Tipo de documento | {artigo revisado por pares, teses/dissertações, anais} |
| `knowledge_area` | Área principal do conhecimento | {ciências da saúde; multidisciplinar; correlata} |
| `country_region` | País/região a que o estudo se refere | Código ISO ou nome padronizado |
| `objective_summary` | Resumo do objetivo principal | 1 a 2 frases |
| `study_design` | Delineamento metodológico | {survey, entrevista, métodos mistos, estudo de caso, usabilidade, outro} |
| `participant_characteristics` | Vínculo, etapa da carreira, disciplina | Descritivo qualitativo |
| `participant_count` | Quantidade de participantes | Ex.: n = 45 (total e subtotais) |
| `support_actors_mentioned` | Atores de apoio relatados | {bibliotecários, data stewards, financiadores, gestores, curadores, TI, outros} |
| `dmp_context_and_requirement` | Contexto e natureza da exigência | Contexto: {financiado, política, periódico}; Exigência: {obrigatório, recomendado, voluntário} |
| `tools_or_platforms_mentioned` | Ferramentas digitais de PGD | {DMPTool, DMPonline, ARGOS, FioDMP, institucional, outra, nenhuma} |
| `perceptions_summary` | Síntese das percepções narrativas | Utilidade, burocracia, relevância, aplicabilidade (com página/seção) |
| `practices_reported` | Práticas relatadas no ciclo de vida | Elaboração, atualização, consulta, monitoramento, conformidade |
| `cost_factors` | Fatores de custo (Modelo MFDados) | {desconhecimento, falta de capacitação/tempo, burocracia, LGPD/sensíveis, infraestrutura, etc.} |
| `benefit_factors` | Fatores de benefício (Modelo MFDados) | Organização, planejamento, reprodutibilidade, segurança, economia de tempo |
| `contextual_institutional_factors` | Condições institucionais | {políticas, normas, infraestrutura, bibliotecas/stewards, incentivos, periódicos, TI} |
| `contextual_individual_factors` | Condições individuais | {conhecimento prévio, familiaridade FAIR, tempo disponível, atitudes, resistência} |
| `facilitators_reported` | Facilitadores relatados | Treinamentos, modelos claros, suporte, integração com repositórios |
| `benefits_perceived` | Checklist controlado de benefícios | Checklist analítico de múltiplos itens |
| `fair_knowledge` | Nível de conhecimento dos Princípios FAIR | {alto, moderado, baixo, não relatado} |
| `data_sharing_reuse_practices` | Práticas de compartilhamento/reuso | Depósito, restrições, licenciamento, metadados |
| `usability_user_experience` | Usabilidade das ferramentas | Interface, clareza, barreiras técnicas |
| `institutional_context_scope` | Escopo institucional | {equipe/lab, departamento, instituição, financiador, nacional, internacional} |
| `recommendations_key` | Recomendações apontadas | Síntese de melhorias para templates, políticas e ferramentas |
| `limitations_flag` | Limitações relatadas | Amostra, viés disciplinar, desenho metodológico |
| `extraction_reviewer` | Iniciais do revisor | Ex.: AA |
| `extraction_date` | Data da extração | AAAA-MM-DD |
| `comments` | Observações adicionais | Notas livres |

---

## 5. Análise e Síntese
* **Síntese:** Análise temática e narrativa guiada pelos objetivos, PCC e Modelo MFDados.
* **Visualização:** Tabelas de distribuição, matrizes temáticas e fluxograma PRISMA-ScR em `documentos/figuras/`.