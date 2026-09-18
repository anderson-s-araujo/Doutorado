import csv
import sys
from pathlib import Path

# Caminho para o arquivo CSV de extração
CSV_PATH = Path("dados/processados/extracao_estudos.csv")

# 1. Definição esperada dos 30 campos na ordem exata do protocolo
COLUNAS_ESPERADAS = [
    "study_id", "citation", "doi_or_url", "document_type", "knowledge_area",
    "country_region", "objective_summary", "study_design", "participant_characteristics",
    "participant_count", "support_actors_mentioned", "dmp_context_and_requirement",
    "tools_or_platforms_mentioned", "perceptions_summary", "practices_reported",
    "cost_factors", "benefit_factors", "contextual_institutional_factors",
    "contextual_individual_factors", "facilitators_reported", "benefits_perceived",
    "fair_knowledge", "data_sharing_reuse_practices", "usability_user_experience",
    "institutional_context_scope", "recommendations_key", "limitations_flag",
    "extraction_reviewer", "extraction_date", "comments"
]

# 2. Listas de valores válidos para colunas com categorias controladas
VALORES_PERMITIDOS = {
    "document_type": [
        "artigo revisado por pares", "teses e dissertações", "anais",
        "relatório técnico", "outro", "NR", "NA"
    ],
    "fair_knowledge": ["alto", "moderado", "baixo", "não relatado", "NR", "NA"]
}

def validar_csv():
    if not CSV_PATH.exists():
        print(f"❌ Erro: Arquivo não encontrado em {CSV_PATH.resolve()}")
        sys.exit(1)

    erros = []
    ids_registrados = set()
    total_linhas = 0

    with open(CSV_PATH, mode="r", encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        try:
            cabecalho = next(reader)
        except StopIteration:
            print("❌ Erro: O arquivo CSV está vazio!")
            sys.exit(1)

        # Validação 1: Número e nomes das colunas
        if cabecalho != COLUNAS_ESPERADAS:
            if len(cabecalho) != len(COLUNAS_ESPERADAS):
                erros.append(
                    f"Número incorreto de colunas: esperadas {len(COLUNAS_ESPERADAS)}, "
                    f"encontradas {len(cabecalho)}."
                )
            diferencas = set(COLUNAS_ESPERADAS) ^ set(cabecalho)
            if diferencas:
                erros.append(f"Divergência nos nomes das colunas: {diferencas}")
        else:
            print("✔ Cabeçalho: 30 campos validados com sucesso.")

        # Validação 2: Checagem linha por linha
        for idx, linha in enumerate(reader, start=2):
            total_linhas += 1
            if len(linha) != len(COLUNAS_ESPERADAS):
                erros.append(
                    f"Linha {idx}: possui {len(linha)} campos (esperado: {len(COLUNAS_ESPERADAS)})."
                )
                continue

            registro = dict(zip(cabecalho, linha))

            # Validação do study_id (duplicações e vazios)
            sid = registro.get("study_id", "").strip()
            if not sid:
                erros.append(f"Linha {idx}: campo 'study_id' está em branco.")
            elif sid in ids_registrados:
                erros.append(f"Linha {idx}: study_id duplicado '{sid}'.")
            else:
                ids_registrados.add(sid)

            # Validação de campos categóricos fechados
            for campo, permitidos in VALORES_PERMITIDOS.items():
                valor = registro.get(campo, "").strip().lower()
                if valor and valor not in [p.lower() for p in permitidos]:
                    erros.append(
                        f"Linha {idx}: valor inválido '{registro[campo]}' no campo '{campo}'."
                    )

    # Relatório final
    print("-" * 50)
    if erros:
        print(f"⚠️ Foram encontrados {len(erros)} apontamentos de inconsistência:")
        for e in erros:
            print(f" - {e}")
    else:
        print(f"✔ Sucesso: Nenhuma inconsistência encontrada.")
        print(f"✔ Total de registros válidos analisados: {total_linhas}")
    print("-" * 50)

if __name__ == "__main__":
    validar_csv()