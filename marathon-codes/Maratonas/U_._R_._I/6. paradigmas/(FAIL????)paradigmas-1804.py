# U.R.I. - 1804 - 6. Paradigmas - Greedy, Ad-Hoc - Agosto de 2019

# Juliano é fã do programa de auditório Apagando e Ganhando, 
# um programa no qual os participantes são selecionados através
#  de um sorteio e recebem prêmios em dinheiro por participarem.

# No programa, o apresentador escreve um número de N dígitos em 
# uma lousa. O participante então deve apagar exatamente D dígitos
#  do número que está na lousa; o número formado pelos dígitos que 
# restaram é então o prêmio do participante.

# Juliano finalmente foi selecionado para participar do programa,
#  e pediu que você escrevesse um programa que, dados o número que 
# o apresentador escreveu na lousa, e quantos dígitos Juliano tem 
# que apagar, determina o valor do maior prêmio que Juliano pode ganhar.

# Entrada
# A entrada contém vários casos de teste. A primeira linha de cada 
# caso de teste contém dois inteiros N e D (1 ≤ D < N ≤ 105), indicando
#  a quantidade de dígitos do número que o apresentador escreveu na lousa
#  e quantos dígitos devem ser apagados. A linha seguinte contém o número
#  escrito pelo apresentador, que não contém zeros à esquerda.

# O final da entrada é indicado por uma linha que contém apenas dois zeros,
#  separados por um espaço em branco.

# Saída
# Para cada caso de teste da entrada seu programa deve imprimir 
# uma única linha na saída, contendo o maior prêmio que Juliano pode ganhar.

# Exemplo de Entrada	Exemplo de Saída
# 4 2
# 3759                # 79
# 6 3
# 123123              # 323
# 7 4
# 1000000             # 100
# 7 3
# 1001234             # 1234
# 6 2
# 103759              # 3759
# 0 0

# Solução: Greedy: apagar os menores primeiro. Ordeno a lista de string e dou um pop em ordem descrecente
# Não é ordenar, ele tem que manter a mesma posicao

# 7 2
# 9909099 = 99999
# 7 3
# 1010101 = 1111
# 0 0

while(True):

  digit, remove_numbers = list(map(int, input().split()))
  if( digit == 0 and remove_numbers == 0):
    break
  number = input()

  aDict = {}
  c = 0
  for i in number:
    aDict[c] = i
    c += 1
  
  print(aDict)
  aDict = sorted(aDict.items(), key = lambda x : x[1])

  aKeys = aDict.keys(

  print(aDict))

  # for _ in range(remove_numbers):
    
  #   pass

  ####################################################33

  # sorted_numbers = sorted(number)
  # for _ in range(remove_numbers):
  #   number = number.replace(sorted_numbers.pop(0), '', 1)
    
  # print(number)


  # sorted_numbers = sorted(number)
  # for _ in range(remove_numbers):
  #   number = number.replace(sorted_numbers.pop(0), '', 1)