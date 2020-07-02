# URI - String - #1024 - Criptografia

# => Na primeira passada, somente caracteres que sejam letras minúsculas 
# e maiúsculas devem ser deslocadas 3 posições para a direita, segundo 
# a tabela ASCII: letra 'a' deve virar letra 'd', letra 'y' deve virar 
# caractere '|' e assim sucessivamente. 
# => Na segunda passada, a linha deverá ser invertida. 
# => Na terceira e última passada, todo e qualquer 
# caractere a partir da metade em diante (truncada) devem ser deslocados 
# uma posição para a esquerda na tabela ASCII. Neste caso, 'b' vira 'a' e 'a' vira '`'.

# Por exemplo, se a entrada for “Texto #3”, o primeiro processamento 
# sobre esta entrada deverá produzir “Wh{wr #3”. O resultado do segundo 
# processamento inverte os caracteres e produz “3# rw{hW”. Por último, 
# com o deslocamento dos caracteres da metade em diante, o resultado final deve ser “3# rvzgV”.

# >>> ord('a')
# 97
# >>> chr(97)
# 'a'
# >>> chr(ord('a') + 3)
# 'd'



def pass1(s):
  l = ""
  for i in s:
    if( i.isalpha()):
      l = l + chr(ord(i) + 3)
    else:
      l = l + i
  return l

def pass2(s):
  return reverse_list(s)

def pass3(s):
  # range(len(s)//2, len(s))
  l = ""
  for index in range(len(s)):
    i = s[index]
    if( index+1 > len(s)//2):
      l = l + chr(ord(i) - 1)
    else:
      l = l + i
  return l

def reverse_list(s):
    temp_list = list(s)
    temp_list.reverse()
    return ''.join(temp_list)

n = int(input())

for i in range(n):
  x = input()
  print(pass3(pass2(pass1(x))))