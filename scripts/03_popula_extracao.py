import csv
from pathlib import Path

# Caminho para o ficheiro CSV de extração
csv_path = Path("dados/processados/extracao_estudos.csv")

# Nova linha validada do estudo S001 (com 30 campos + categoria)
novo_estudo = [
    "S001",
    "Adapting the DMPTool to support NIH HEAL Initiative data sharing policies",
    "https://doi.org/10.1093/jamiaopen/ooaf040",
    "Relato de experiência / Aplicação tecnológica (Application Note)",
    "Ciências da Saúde / Gestão de Dados",
    "Estados Unidos da América (EUA)",
    "Descrever a adaptação do DMPTool para suportar as políticas de partilha de dados da iniciativa NIH HEAL.",
    "Relato de experiência / Aplicação tecnológica",
    "Investigadores financiados pelo consórcio HEAL / dor crónica e adicção; HEAL Data Stewardship Group",
    "Não relatado / Não se aplica",
    "data stewards; gestores de repositório; financiadores",
    "Projeto financiado / Obrigatório",
    "DMPTool",
    "Redução de encargo administrativo e suporte à conformidade",
    "Respostas-modelo, registo HEAL Platform, metadados CEDAR, uso de CDEs e depósito NAHDAP",
    "dados sensíveis; privacidade e confidencialidade; carga burocrática; ausência de modelos adaptados",
    "conformidade com políticas; princípios FAIR; redução da carga de trabalho; colaboração",
    "exigências de financiadores; políticas e normas; suporte de bibliotecas ou data stewards; repositórios; infraestrutura",
    "percepção de utilidade; familiaridade com PGD; familiaridade com FAIR; disponibilidade de tempo",
    "Templates com exemplos integrados, HEAL Stewards, interfaces padronizadas (CEDAR) e equipas de apoio de repositórios",
    "aumento do potencial de compartilhamento; facilitação da colaboração; maior conformidade; metadados; economia de tempo",
    "não relatado",
    "Depósito NAHDAP (aberto e restrito), registo HEAL, metadados CEDAR, termos com anonimização, CDEs",
    "Avaliação positiva com interface guiada passo a passo no DMPTool",
    "financiador (âmbito nacional dos EUA - NIH/NIDA)",
    "PGD vivo precoce; modelos orientados; CDEs; consulta antecipada a curadores e repositórios",
    "Foco restrito ao consórcio NIH HEAL; ausência de estudo longitudinal com amostra grande",
    "AA",
    "2026-09-20",
    "Estudo S001 validado detalhadamente conforme relatório completo.",
    "DMPTool"
]

def atualizar_ou_inserir_estudo():
    if not csv_path.exists():
        print(f"Erro: O ficheiro {csv_path} não foi encontrado.")
        return

    linhas = []
    cabecalho = None
    atualizado = False
    
    # Ler o ficheiro existente
    with open(csv_path, mode="r", encoding="utf-8") as f:
        leitor = csv.reader(f)
        for i, linha in enumerate(leitor):
            if i == 0:
                cabecalho = linha
                continue
            if linha and linha[0] == novo_estudo[0]:
                linhas.append(novo_estudo) # Substitui o S001 antigo pelo novo
                atualizado = True
            else:
                linhas.append(linha)
                
    if not atualizado:
        linhas.append(novo_estudo)
        
    # Escrever de volta para o CSV preservando o cabeçalho original
    with open(csv_path, mode="w", encoding="utf-8", newline="") as f:
        escritor = csv.writer(f)
        if cabecalho:
            escritor.writerow(cabecalho)
        escritor.writerows(linhas)
        
    print(f"Sucesso! Estudo {novo_estudo[0]} atualizado com 30 campos, mantendo os restantes registos intactos.")

if __name__ == "__main__":
    atualizar_ou_inserir_estudo()