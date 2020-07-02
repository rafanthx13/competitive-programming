# A sua impressora foi infectada por um vírus e está imprimindo de forma incorreta. 
# Depois de olhar para várias páginas impressas por um tempo, você percebe que ele 
# está imprimindo cada linha de dentro para fora. Em outras palavras, a metade esquerda
# de cada linha está sendo impressa a partir do meio da página até a margem esquerda. 
# Do mesmo modo, a metade direita de cada linha está sendo impressa à partir da margem 
# direita e prosseguindo em direção ao centro da página.


# Por exemplo a linha:
# THIS LINE I|S GIBBERISH (22 LETTRAS SEPARAOU EM 11)
  # [REVERSE]+[REVERSE]
# está sendo impressa como:
# I ENIL SIHTHSIREBBIG S

# FRENCH HENS TWO |DOVES AND A PARTRIDGE
# VOD OWT SNEH HCNERF EGDIRTRAP A DNA SE

# Da mesma foma, a linha " MANGOS " está sendo impressa incorretamente como "NAM  SOG". 
# Sua tarefa é desembaralhar (decifrar) a string a partir da forma como ela foi impressa 
# para a sua forma original. Você pode assumir que cada linha conterá um número par de caracteres.

# Entrada
# A entrada contém vários casos de teste. A primeira linha de entrada contém um inteiro N que indica
#  a quantidade de casos de teste. Seguem N linhas, cada uma com uma frase com no mínimo 2 e no máximo
#  100 caracteres de letras maiúsculas e espaços que deverá ser desembaralhada (decifrada) à partir da
#  forma impressa para a sua forma original, conforme especificação acima.

# Saída
# Para cada linha de entrada deverá ser impressa uma linha de saída com a frase decifrada, conforme a especificação acima.

#       Exemplo de Entrada	
# 5
# I ENIL SIHTHSIREBBIG S
# LEVELKAYAK
# H YPPAHSYADILO
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# VOD OWT SNEH HCNERF EGDIRTRAP A DNA SE

#       Exemplo de Saída
# THIS LINE IS GIBBERISH
# LEVELKAYAK
# HAPPY HOLIDAYS
# MLKJIHGFEDCBAZYXWVUTSRQPON
# FRENCH HENS TWO DOVES AND A PARTRIDGE

import math

def reverse_all_string(s):
  ss = ''
  l = len(s)
  for i in range(l):
    ss = ss + s[(l-1)-i]
  return ss

n = int(input())

for i in range(n):
  w = input()
  half = math.ceil(len(w)/2)
  print(reverse_all_string(w[:half]) + reverse_all_string(w[half:]))
  