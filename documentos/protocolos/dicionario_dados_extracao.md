# Dicionário de Dados (Codebook) - Ficha de Extração
**Estudo:** Percepções e práticas dos pesquisadores em relação aos PGDs e ferramentas de PGD  
**Ficheiro associado:** `dados/processados/extracao_estudos.csv`  
**Referencial analítico:** Metodologia JBI (Scoping Review) e Modelo MFDados  
**Data da versão:** 2026-09-18  

---

## Orientações Gerais de Preenchimento
* **Codificação:** UTF-8.
* **Separador de valores:** Vírgula (`,`). Quando um campo contiver texto com vírgulas ou quebras de linha, delimitar obrigatoriamente com aspas duplas (`"..."`).
* **Campos de múltipla seleção:** Separar termos permitidos com ponto e vírgula (`;`).
* **Dados ausentes/não relatados:** Preencher com `NR` (Não Relatado) ou `NA` (Não Aplicável).

---

## Dicionário de Variáveis (30 Campos)

| # | Nome do Campo | Tipo de Dado | Valores Permitidos / Regras de Preenchimento | Exemplo / Orientação |
| :-: | :--- | :--- | :--- | :--- |
| **1** | `study_id` | Texto (identificador) | Código alfanumérico único derivado da triagem (Rayyan). | `S001`, `S042` |
| **2** | `citation` | Texto | Citação bibliográfica padronizada em estilo Vancouver. | `Silva AB, Santos CD, 2023` |
| **3** | `doi_or_url` | Texto (URL/URI) | Formato `https://doi.org/10.xxxx/...` (prioritário) ou link persistente. | `https://doi.org/10.1016/j.jbi.2023.1001` |
| **4** | `document_type` | Categórico | `artigo revisado por pares`, `teses e dissertações`, `anais`, `relatório técnico`, `outro` | Seleção única da categoria principal. |
| **5** | `knowledge_area` | Categórico | `ciências da saúde`, `multidisciplinar com interface na saúde`, `outra área correlata à saúde – especificar` | Baseado em título, resumo e palavras-chave. |
| **6** | `country_region` | Texto padronizado | Nome padronizado do país ou território investigado (não a afiliação dos autores). | `Brasil`, `Portugal`, `Estados Unidos` |
| **7** | `objective_summary` | Texto livre | Síntese direta do objetivo em 1 ou 2 frases curtas. | `"Mapear percepções de docentes sobre DMPTool."` |
| **8** | `study_design` | Categórico | `survey`, `entrevista`, `métodos mistos`, `estudo de caso`, `revisão`, `guia`, `política`, `relato de experiência`, `estudo de usabilidade`, `outro` | Delineamento metodológico principal. |
| **9** | `participant_characteristics` | Texto descritivo | Vínculo institucional, estágio da carreira, área disciplinar ou função. | `"Docentes permanentes e pós-graduandos em Saúde Pública."` |
| **10** | `participant_count` | Texto / Numérico | Quantidade total e subtotais relatados. | `n = 45 (30 pesquisadores; 15 pós-graduandos)` |
| **11** | `support_actors_mentioned` | Múltipla seleção | `bibliotecários`, `data stewards`, `financiadores`, `gestores de repositório`, `desenvolvedores`, `curadores`, `editores`, `equipes de tecnologia`, `outros – especificar`, `nenhum` | Separar por `;` caso haja mais de um. |
| **12** | `dmp_context_and_requirement` | Estruturado | Contexto: `{projeto financiado; política institucional; periódico; repositório; curso/treinamento; ferramenta digital; outro}` \| Exigência: `{obrigatório; recomendado; voluntário; não relatado}` | `Contexto: projeto financiado; Exigência: obrigatório` |
| **13** | `tools_or_platforms_mentioned` | Múltipla seleção | `DMPTool`, `DMPonline`, `ARGOS`, `FioDMP`, `ferramenta institucional`, `outra – especificar`, `nenhuma` | Incluir versão ou desenvolvedor entre parênteses se constar. |
| **14** | `perceptions_summary` | Texto livre | Síntese qualitativa de atitudes, utilidade, barreiras percebidas, com página ou secção da evidência. | `"Pesquisadores encaram como burocracia excessiva (p. 4)."` |
| **15** | `practices_reported` | Texto livre | Ações concretas no ciclo de dados: elaboração, atualização, consulta, monitoramento, conformidade. | `"Atualização realizada apenas no relatório final (p. 6)."` |
| **16** | `cost_factors` | Múltipla seleção (MFDados) | `desconhecimento sobre PGD`, `falta de capacitação`, `falta de tempo`, `carga burocrática`, `resistência à mudança`, `dados sensíveis`, `privacidade`, `confidencialidade`, `direitos autorais`, `propriedade intelectual`, `licenciamento`, `adequação à LGPD`, `ausência de modelos adaptados`, `falta de suporte`, `recursos insuficientes`, `infraestrutura insuficiente`, `outro – especificar` | Classificação analítica de custos percebidos. |
| **17** | `benefit_factors` | Múltipla seleção (MFDados) | `organização`, `planejamento`, `qualidade`, `colaboração`, `eficiência`, `reprodutibilidade`, `compartilhamento`, `conformidade`, `preservação`, `metadados`, `economia de tempo`, `impacto científico`, `serviços`, `políticas`, `incentivos`, `ferramentas`, `outro – especificar` | Categorias conceituais de benefício (MFDados). |
| **18** | `contextual_institutional_factors`| Múltipla seleção (MFDados) | `políticas`, `normas`, `infraestrutura`, `serviços de apoio`, `suporte de bibliotecas ou data stewards`, `incentivos`, `exigências de financiadores`, `exigências de periódicos`, `cultura organizacional`, `repositórios`, `equipes de tecnologia`, `outro – especificar` | Condições externas que moldam o comportamento. |
| **19** | `contextual_individual_factors` | Múltipla seleção (MFDados) | `conhecimento prévio`, `experiência com gestão de dados`, `familiaridade com PGD`, `familiaridade com FAIR`, `habilidades informacionais`, `disponibilidade de tempo`, `atitudes`, `valores`, `resistência à mudança`, `percepção de utilidade`, `outro – especificar` | Características e competências do sujeito. |
| **20** | `facilitators_reported` | Texto livre | Descrição pontual dos facilitadores explícitos acompanhada da respetiva página ou secção. | `"Disponibilidade de modelos pré-configurados pela biblioteca (p. 7)."` |
| **21** | `benefits_perceived` | Múltipla seleção (Checklist) | Checklist controlado: `Melhor organização dos dados`, `Planejamento antecipado`, `Maior qualidade dos dados`, `Facilitação da colaboração`, `Redução de perda de dados`, `Maior eficiência durante a pesquisa`, `Facilitação da reprodutibilidade`, `Aumento do potencial de compartilhamento`, `Maior conformidade ética e legal`, `Maior clareza sobre metadados/armazenamento/preservação`, `Economia de tempo`, `Impacto científico`, `outro – especificar` | Separar opções selecionadas com `;`. |
| **22** | `fair_knowledge` | Categórico | `alto`, `moderado`, `baixo`, `não relatado` | Grau de familiaridade dos participantes com os Princípios FAIR. |
| **23** | `data_sharing_reuse_practices` | Texto descritivo | Relato de depósito em repositório, atribuição de licença ou barreiras éticas/legais associadas. | `"Depósito efetuado no Zenodo sob licença CC-BY (p. 5)."` |
| **24** | `usability_user_experience` | Texto descritivo | Avaliações relativas à interface, facilidade de uso, termos obscuros ou integração no fluxo de trabalho. | `"Campos técnicos de ontologias considerados difíceis (p. 8)."` |
| **25** | `institutional_context_scope` | Categórico | `equipe ou laboratório`, `departamento`, `instituição`, `financiador`, `periódico`, `repositório`, `nível nacional`, `nível internacional`, `outro – especificar` | Escopo de aplicação institucional. |
| **26** | `recommendations_key` | Texto livre | Propostas e sugestões relatadas pelos autores ou participantes do estudo. | `"Capacitação contínua e simplificação dos modelos de PGD."` |
| **27** | `limitations_flag` | Texto livre | Vieses, amostras reduzidas ou fragilidades metodológicas registadas no estudo. | `"Amostra não probabilística restrita a uma única instituição."` |
| **28** | `extraction_reviewer` | Texto (Iniciais) | Iniciais do revisor responsável pelo preenchimento da linha. | `AA`, `CB`, `IH` |
| **29** | `extraction_date` | Data | Formato padrão ISO: `AAAA-MM-DD`. | `2026-09-18` |
| **30** | `comments` | Texto livre | Observações complementares, dúvidas de categorização ou notas de consenso. | `"Consenso obtido com o terceiro revisor em reunião de equipe."` |