import csv
from datetime import date
from pathlib import Path

ARQUIVO_RAYYAN = Path("dados/brutos/rayyan_incluidos.csv")
ARQUIVO_SAIDA = Path("dados/processados/extracao_estudos.csv")

COLUNAS_OFICIAIS = [
    "study_id",
    "citation",
    "doi_or_url",
    "document_type",
    "knowledge_area",
    "country_region",
    "objective_summary",
    "study_design",
    "participant_characteristics",
    "participant_count",
    "support_actors_mentioned",
    "dmp_context_and_requirement",
    "tools_or_platforms_mentioned",
    "perceptions_summary",
    "practices_reported",
    "cost_factors",
    "benefit_factors",
    "contextual_institutional_factors",
    "contextual_individual_factors",
    "facilitators_reported",
    "benefits_perceived",
    "fair_knowledge",
    "data_sharing_reuse_practices",
    "usability_user_experience",
    "institutional_context_scope",
    "recommendations_key",
    "limitations_flag",
    "extraction_reviewer",
    "extraction_date",
    "comments",
]


def formatar_citacao(autores, ano):
  ano_str = str(ano).strip() if ano else "s.d."
  if not autores:
    return f"Autor Desconhecido, {ano_str}"

  lista_autores = [
      a.strip() for a in autores.replace(" and ", ";").split(";") if a.strip()
  ]
  if not lista_autores:
    return f"Autor Desconhecido, {ano_str}"

  primeiro = lista_autores[0].split(",")[0].strip()
  if len(lista_autores) == 1:
    return f"{primeiro}, {ano_str}"
  elif len(lista_autores) == 2:
    segundo = lista_autores[1].split(",")[0].strip()
    return f"{primeiro} & {segundo}, {ano_str}"
  else:
    return f"{primeiro} et al., {ano_str}"


def obter_dado(linha, *chaves):
  for chave in chaves:
    valor = linha.get(chave, "").strip()
    if valor:
      return valor
  return ""


def main():
  if not ARQUIVO_RAYYAN.exists():
    print(f"Erro: Arquivo do Rayyan não encontrado em: {ARQUIVO_RAYYAN}")
    return

  with open(ARQUIVO_RAYYAN, mode="r", encoding="utf-8-sig") as f_in:
    reader = csv.DictReader(f_in)
    estudos_rayyan = list(reader)

  total = len(estudos_rayyan)
  print(f"Lendo {total} estudos incluídos do Rayyan...")

  hoje = date.today().strftime("%Y-%m-%d")
  linhas_processadas = []

  for idx, linha in enumerate(estudos_rayyan, start=1):
    sid = f"S{idx:03d}"

    autores = linha.get("authors", "")
    ano = linha.get("year", "")
    citacao = obter_dado(linha, "208088-citation") or formatar_citacao(
        autores, ano
    )

    doi = linha.get("doi", "").strip()
    url = linha.get("url", "").strip()
    link = doi if doi else url
    if link and not link.startswith("http") and "10." in link:
      link = f"https://doi.org/{link}"
    doi_final = obter_dado(linha, "208101-doi_or_url") or link or "NR"

    resumo = (
        obter_dado(linha, "208112-objective_summary")
        or linha.get("abstract", "").strip()
        or linha.get("title", "").strip()
        or "NR"
    )

    doc_type = (
        obter_dado(linha, "208109-document_type")
        or "artigo revisado por pares"
    )
    knowledge_area = (
        obter_dado(linha, "208110-knowledge_area") or "ciências da saúde"
    )
    country_region = obter_dado(linha, "208111-country_region") or "NR"
    study_design = obter_dado(linha, "208113-study_design") or "NR"
    part_char = (
        obter_dado(linha, "208114-participant_characteristics")
        or "pesquisadores"
    )
    part_count = obter_dado(linha, "208115-participant_count") or "NR"
    actors = (
        obter_dado(linha, "222317-support_actors_mentioned")
        or "bibliotecários; data stewards"
    )

    registro = {
        "study_id": sid,
        "citation": citacao,
        "doi_or_url": doi_final,
        "document_type": doc_type,
        "knowledge_area": knowledge_area,
        "country_region": country_region,
        "objective_summary": resumo,
        "study_design": study_design,
        "participant_characteristics": part_char,
        "participant_count": part_count,
        "support_actors_mentioned": actors,
        "dmp_context_and_requirement": "NR",
        "tools_or_platforms_mentioned": "NR",
        "perceptions_summary": "NR",
        "practices_reported": "NR",
        "cost_factors": "NR",
        "benefit_factors": "NR",
        "contextual_institutional_factors": "NR",
        "contextual_individual_factors": "NR",
        "facilitators_reported": "NR",
        "benefits_perceived": "NR",
        "fair_knowledge": "NR",
        "data_sharing_reuse_practices": "NR",
        "usability_user_experience": "NR",
        "institutional_context_scope": "NR",
        "recommendations_key": "NR",
        "limitations_flag": "NR",
        "extraction_reviewer": "AA",
        "extraction_date": hoje,
        "comments": (
            f"Registro importado do Rayyan (key: {linha.get('key', '')})."
        ),
    }
    linhas_processadas.append(registro)

  with open(ARQUIVO_SAIDA, mode="w", encoding="utf-8-sig", newline="") as f_out:
    writer = csv.DictWriter(f_out, fieldnames=COLUNAS_OFICIAIS)
    writer.writeheader()
    writer.writerows(linhas_processadas)

  print(
      f"✔ Sucesso: {len(linhas_processadas)} estudos transferidos para"
      f" {ARQUIVO_SAIDA}"
  )


if __name__ == "__main__":
  main()