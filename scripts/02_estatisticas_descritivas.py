import csv
from collections import Counter
from pathlib import Path

CSV_PATH = Path("dados/processados/extracao_estudos.csv")


def sintetizar_campo_multivalorado(registros, campo):
  termos = []
  for r in registros:
    conteudo = r.get(campo, "").strip()
    if conteudo and conteudo not in ["NR", "NA"]:
      itens = [item.strip() for item in conteudo.split(";") if item.strip()]
      termos.extend(itens)
  return Counter(termos)


def gerar_relatorio():
  if not CSV_PATH.exists():
    print(f"Erro: Arquivo não localizado em {CSV_PATH}")
    return

  with open(CSV_PATH, mode="r", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    registros = list(reader)

  total = len(registros)
  print("=" * 60)
  print(f"SÍNTESE DESCRITIVA DA EXTRAÇÃO (N = {total} estudos)")
  print("=" * 60)

  if total == 0:
    print("Nenhum estudo registrado para análise.")
    return

  # 1. Delineamento de estudo
  print("\n1. Delineamento Metodológico (study_design):")
  designs = Counter(
      r.get("study_design", "NR").strip()
      for r in registros
      if r.get("study_design")
  )
  for k, v in designs.most_common():
    print(f"   - {k}: {v} ({v/total*100:.1f}%)")

  # 2. Distribuição Geográfica
  print("\n2. Distribuição Geográfica (country_region):")
  paises = Counter(
      r.get("country_region", "NR").strip()
      for r in registros
      if r.get("country_region")
  )
  for k, v in paises.most_common(5):
    print(f"   - {k}: {v} ({v/total*100:.1f}%)")

  # 3. Ferramentas e Plataformas Mencionadas (multivalorado)
  print("\n3. Ferramentas e Plataformas (tools_or_platforms_mentioned):")
  ferramentas = sintetizar_campo_multivalorado(
      registros, "tools_or_platforms_mentioned"
  )
  for k, v in ferramentas.most_common():
    print(f"   - {k}: {v} ocorrência(s)")

  # 4. Fatores de Custo (MFDados - multivalorado)
  print("\n4. Fatores de Custo Relatados (cost_factors):")
  custos = sintetizar_campo_multivalorado(registros, "cost_factors")
  for k, v in custos.most_common():
    print(f"   - {k}: {v} ocorrência(s)")

  # 5. Fatores de Benefício (MFDados - multivalorado)
  print("\n5. Fatores de Benefício Relatados (benefit_factors):")
  beneficios = sintetizar_campo_multivalorado(registros, "benefit_factors")
  for k, v in beneficios.most_common():
    print(f"   - {k}: {v} ocorrência(s)")

  print("\n" + "=" * 60)


if __name__ == "__main__":
  gerar_relatorio()