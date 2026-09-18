# /// script
# dependencies = [
#   "matplotlib",
# ]
# ///

import csv
from collections import Counter
from pathlib import Path
import matplotlib.pyplot as plt

CSV_PATH = Path("dados/processados/extracao_estudos.csv")
FIGURAS_DIR = Path("documentos/figuras")


def sintetizar_campo_multivalorado(registros, campo):
  termos = []
  for r in registros:
    conteudo = r.get(campo, "").strip()
    if conteudo and conteudo not in ["NR", "NA"]:
      itens = [item.strip() for item in conteudo.split(";") if item.strip()]
      termos.extend(itens)
  return Counter(termos)


def salvar_grafico_barras(contador, titulo, nome_arquivo, rotulo_x="Frequência"):
  if not contador:
    return

  FIGURAS_DIR.mkdir(parents=True, exist_ok=True)
  itens_ordenados = contador.most_common()
  categorias = [k for k, _ in itens_ordenados]
  valores = [v for _, v in itens_ordenados]

  plt.figure(figsize=(9, 5))
  plt.barh(categorias[::-1], valores[::-1], color="#2b5c8f")
  plt.xlabel(rotulo_x)
  plt.title(titulo, fontsize=12, fontweight="bold")
  plt.tight_layout()

  saida = FIGURAS_DIR / nome_arquivo
  plt.savefig(saida, dpi=300)
  plt.close()
  print(f"✔ Gráfico salvo: {saida}")


def gerar_relatorio_e_graficos():
  if not CSV_PATH.exists():
    print(f"Erro: Arquivo não localizado em {CSV_PATH}")
    return

  with open(CSV_PATH, mode="r", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    registros = list(reader)

  total = len(registros)
  if total == 0:
    print("Nenhum estudo registrado para análise.")
    return

  print("=" * 60)
  print(f"GERANDO ESTATÍSTICAS E GRÁFICOS (N = {total} estudos)")
  print("=" * 60)

  ferramentas = sintetizar_campo_multivalorado(
      registros, "tools_or_platforms_mentioned"
  )
  custos = sintetizar_campo_multivalorado(registros, "cost_factors")
  beneficios = sintetizar_campo_multivalorado(registros, "benefit_factors")

  salvar_grafico_barras(
      ferramentas,
      "Ferramentas e Plataformas de PGD Mencionadas",
      "grafico_ferramentas.png",
  )
  salvar_grafico_barras(
      custos, "Fatores de Custo Relatados (MFDados)", "grafico_custos.png"
  )
  salvar_grafico_barras(
      beneficios,
      "Fatores de Benefício Relatados (MFDados)",
      "grafico_beneficios.png",
  )


if __name__ == "__main__":
  gerar_relatorio_e_graficos()