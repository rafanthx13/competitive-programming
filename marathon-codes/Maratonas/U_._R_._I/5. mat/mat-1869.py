# U_R_I - 4. Mat - Agosto de 2019 - Assunto: Converter para outra base (32) [All right]

# Num país chamado Tresdoislândia, todos os números são tratados na base 32, na qual 
# cada símbolo numérico representa a ordem numérica, e os algarismos seguintes utilizam
#  as letras de A até V. Por exemplo, o número 31 na base 32 é o algarismo V, e o número 32 na base 32 se torna 10.

# Escreva um programa que, dado um número inteiro na base decimal, converta para a base 32.

# Entrada
# Haverá diversos casos de teste. Cada caso de teste inicia com um inteiro N (0 ≤ N ≤ 2^63), 
# indicando um número na base decimal.

# O último caso de teste é indicado quando N = 0.

# Saída
# Para cada caso de teste, imprima o valor correspondente à entrada, na base 32.

# Exemplo de Entrada	Exemplo de Saída
# 31                  # V
# 32                  # 10
# 1024                # 100
# 1300                # 18K
# 0                   # 0

# cria dicionario (h eh global e vem de fora)
h = {}
def dictionary_base31():

  def int_to_char(n):
    return str(chr(n))

  for i in range(10):
    h[i] = str(i)

  start_ascci = ord("A")
  c = 0
  for j in range(10, 32):
    h[j] = int_to_char(start_ascci + c)
    c += 1

dictionary_base31()

# retorna base 32 de um numero n (sendo h dicionario com os simbolos alfabeticos {10: "A", 11: "B", ....})
# Como converter base:
#   Geral: Usa operação de DIvisão e Módulo. Adiciona numa lista e detepois retorna a lista revertida
def base_32(n):
  if(n == 0):
    return "0"
  result = []
  while(n != 0):
    resto = n % 32
    result.append(h[resto]) # insere o simbolo na lista, insere no final
    n = n // 32
  return "".join(result[::-1]) # inverte e junta numa string

# main
while(True):

  result = []
  n = int(input())
  if(n == 0):
    print(0)
    break

  print(base_32(n))