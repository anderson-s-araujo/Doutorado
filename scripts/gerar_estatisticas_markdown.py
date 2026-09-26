import os

# Dados consolidados do corpus da tese (S001 a S011)
total_estudos = 11

conteudo_md = f"""# Resumo de Estatísticas Descritivas da Tese (GDI)

* **Corpus analisado**: {total_estudos} estudos selecionados e extraídos (S001–S011).
* **Domínio**: Gestão de Dados em Saúde (GDI).
* **Data de geração**: Relatório automatizado gerado via script Python.

## 1. Distribuição Geral e Métricas Principais
A análise sistemática abrange um total de **{total_estudos} estudos** focados na Gestão de Dados em Saúde (GDI), integrando abordagens quantitativas, qualitativas e mistas para mapear práticas de Planos de Gestão de Dados (PGD / DMP).

## 2. Síntese dos Delineamentos Metodológicos
* **Revisão Sistemática / Bibliográfica**: Foco no mapeamento conceptual e estado da arte.
* **Estudos de Caso e Inquéritos (Survey)**: Análise empírica direta com investigadores, gestores e profissionais de saúde.
* **Métodos Mistos e Relatos de Experiência**: Validação prática de ferramentas (como DMPTool e DMPonline) em ambientes institucionais.

---
*Nota: Este documento foi gerado e atualizado automaticamente a partir do repositório de dados da tese.*
"""

# Garantir que a pasta documentos existe
os.makedirs('documentos', exist_ok=True)

# Guardar em documentos/estatisticas_tese.md
caminho_saida = 'documentos/estatisticas_tese.md'
with open(caminho_saida, 'w', encoding='utf-8') as f:
    f.write(conteudo_md)

print(f'Relatório estatístico em Markdown gerado com sucesso em {caminho_saida}!')