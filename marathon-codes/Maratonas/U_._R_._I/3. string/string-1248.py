# O doutor deu a você a sua dieta, na qual cada caractere corresponde a 
# algum alimento que você deveria comer. Você também sabe o que você tem
#  comido no café da manha e no almoço, nos quais cada caractere corresponde 
# a um tipo de alimento que você deveria ter comido aquele dia. Você decidiu
#  que irá comer todo o restante de sua dieta durante o jantar, e você quer 
# imprimi-la como uma String (ordenada em ordem alfabética). 
# Se você trapaceou de
#  algum modo (ou por comer muito de tipo de alimento, ou por comer algum alimento
#  que não está no plano de dieta), você deveria imprimir a cadeia "CHEATER" 
# (significa trapaceiro), sem as aspas.

# Entrada
# A entrada contém vários casos de teste. A primeira linha de entrada contém um 
# inteiro N que indica a quantidade de casos de teste. 
# Cada caso de teste é composto 
# por três linhas, cada uma delas com uma string com até 26 caracteres de 'A'-'Z' ou vazia,
#  representando respectivamente os alimentos da dieta, do café da manhã e do almoço.

# Saída
# Para cada caso de teste imprima uma string que representa os alimentos que você 
# deveria consumir no jantar, ou "CHEATER" caso você tenha trapaceado na sua dieta.

#             Exemplo de Entrada	
# 5

# ABCD
# AB
# C

# ABEDCS
# ''
# ''

# EDSMB
# MSD
# A

# ''
# ''
# ''

# IWANTSODER
# SOW
# RAT

#             Exemplo de Saída

# D
# ABCDES
# CHEATER
# ''
# DEIN

# "XOSMQLDFB" ==> "BDFLMOSQX"

# HOW TO DO: Essa é facil mas o problema é a duplciadata de caracters
# Se uma dieta tiver caracter duplicados eles saem na saida, ficando todos os chars distintos
# infelismente nao da pra perceber isso no exemplos.

# Considere o seguinte caso:
# 1
# AUITWOTHOUSAND
# ''
# ''
# OUTPUT : ADHINOSTUW

# Considere o seguinte caso:
# 1
# aaa
# aa
# a
# OUTPUT : CHEATER (DEVE SAIR UM ÚNICO CHEATER)


# "zxya" => "axyz"
def sort_inside_string(s):
  return ''.join(sorted(s))

# "aaaabbbbcccc" => "abc"
def remove_duplicate_char_in_string(s):
  d = {}
  for i in s:
    d[i] = True
  ss = ''
  for key in d:
    ss = ss + key
  return ss

n = int(input())

for i in range(n):

  flag = False
  dieta = input()
  ref1 = input()
  ref2 = input()

  L1 = []
  for i1 in ref1:

    if(i1 in remove_duplicate_char_in_string(dieta)):
      dieta = dieta.replace(i1,"")
    else:
      print("CHEATER")
      flag = True
      continue

  if( not flag):
    for i1 in remove_duplicate_char_in_string(ref2):
      if(i1 in dieta):
        dieta = dieta.replace(i1,"")
      else:
        flag = True
        print("CHEATER")
        continue

  if( not flag):
    print(sort_inside_string(remove_duplicate_char_in_string(dieta)))