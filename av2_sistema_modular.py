# ==============================================================================
# PROVA PRÁTICA AV2 - 3º BIMESTRE
# ARQUIVO: av2_sistema_modular.py
# Nome do Aluno: Rebeca Tresoldi
# Data: 18/09/2026
# Link do Repositório: 
# ==============================================================================
# Lista inicial de dados brutos (Exemplo: Sistema de RH / Atendimento)
# Os dados estão no formato: "nome_completo;cargo_ou_setor;telefone_ou_cpf"
dados_brutos = [
   "  carlos eduardo silva;desenvolvedor;11988887777  ",
   "  ana paula mendes;analista de rh;21977776666  ",
   "  roberto carlos oliveira;gerente de projetos;31966665555  "
]

# ------------------------------------------------------------------------------
# 1. FUNÇÕES DO SISTEMA (Mínimo de 3 funções)
# ------------------------------------------------------------------------------
def limpar_e_formatar_texto(texto):
   """
   FUNÇÃO 1:
   - Recebe uma string.
   - Remove espaços extras das pontas (.strip()).
   - Converte o texto para letras MAIÚSCULAS (.upper()).
   - Retorna o texto devidamente formatado.
   """
   texto_limpo = texto.strip().upper()
   return texto_limpo

def extrair_codigo_ou_ddd(dado):
   """
   FUNÇÃO 2:
   - Recebe um dado em formato de string (ex: telefone ou CPF).
   - Remove espaços das pontas.
   - Utiliza FATIAMENTO DE STRING [x:y] para extrair os 2 primeiros dígitos (DDD).
   - Retorna apenas os dígitos extraídos.
   """
   dado_limpo = dado.strip()
   ddd = dado_limpo[0:2]
   return ddd

def processar_e_exibir_cadastros(lista_dados):
   """
   FUNÇÃO 3:
   - Recebe a lista de cadastros brutos como parâmetro.
   - Utiliza um laço FOR para percorrer cada item da lista.
   - Para cada item:
       1. Separa as partes usando .split(";")
       2. Chama a Função 1 para formatar o Nome e o Cargo.
       3. Chama a Função 2 para extrair o DDD/Código do telefone.
       4. Exibe o resultado final formatado com f-string.
   - Retorna a quantidade total de registros processados.
   """
   total_registros = 0
   
   for registro in lista_dados:
       # Separando o registro pelas ponto e vírgulas
       partes = registro.split(";")
       
       nome_bruto = partes[0]
       cargo_bruto = partes[1]
       telefone_bruto = partes[2]
       
       # Chamando as funções auxiliares
       nome_formatado = limpar_e_formatar_texto(nome_bruto)
       cargo_formatado = limpar_e_formatar_texto(cargo_bruto)
       ddd = extrair_codigo_ou_ddd(telefone_bruto)
       
       # Exibindo o resultado formatado
       print(f"Nome: {nome_formatado} | Cargo: {cargo_formatado} | DDD: {ddd}")
       
       # Incrementando o contador
       total_registros += 1
       
   return total_registros

# ------------------------------------------------------------------------------
# 2. PROGRAMA PRINCIPAL (FLUXO DE EXECUÇÃO)
# ------------------------------------------------------------------------------
def main():
   print("==================================================")
   print("     SISTEMA DE GESTÃO MODULARIZADO - AV2        ")
   print("==================================================\n")
   print("Iniciando o processamento dos dados...\n")
   
   # Chamada da Função 3 armazenando o retorno na variável
   total_processado = processar_e_exibir_cadastros(dados_brutos)
   
   # Exibição da mensagem final com o total retornado
   print(f"\nTotal de registros processados com sucesso: {total_processado}")
   
   print("\n==================================================")
   print("             PROCESSAMENTO CONCLUÍDO              ")
   print("==================================================")

# Execução do programa
if __name__ == "__main__":
   main()
