# Nós temos algumas palavras e queremos justificá-las à direita, ou seja, 
# alinhar todas elas à direita. Crie um programa que, após ler várias palavras
# , reimprima estas palavras com suas linhas justificadas à direita.

# Entrada
# A entrada contém diversos casos de testes. A primeira linha de cada caso 
# de teste conterá um inteiro N (1 ≤ N ≤ 50), que indicará o número de palavras
#  que virão a seguir. Cada uma das N palavras contém no mínimo uma letra e no 
# máximo 50 letras maiúsculas (‘A’-‘Z’). O fim da entrada é indicado por N = 0.

# Saída
# Para cada caso de teste imprima as palavras inserindo tantos espaços quanto 
# forem necessários à esquerda de cada palavra, para que elas apareçam todas 
# alinhadas à direita e na mesma ordem da entrada. Deixe uma linha em branco 
# entre os casos de teste. Não deixe espaços sobrando no final de cada linha 
# nem imprima espaços desnecessários à esquerda, de modo que pelo menos uma 
# das linhas impressa em cada texto inicie com uma letra.

# Exemplo de Entrada	
# 3
# BOB
# TOMMY
# JIM
# 4
# JOHN
# JAKE
# ALAN
# BLUE
# 4
# LONGEST
# A
# LONGER
# SHORT
# 0

# Exemplo de Saída
#   BOB
# TOMMY
#   JIM

# JOHN
# JAKE
# ALAN
# BLUE

# LONGEST
#       A
#  LONGER
#   SHORT

def maxlen(list_tuple):
  q = -1
  for word in list_tuple:
    if(len(word) > q):
      q = len(word)
  return q

qtd = int(input())

while(qtd != 0):
  list_words = []

  for i in range(qtd):
    w = input()
    list_words.append(w)

  max_word = maxlen(list_words)

  for aWord in list_words:
    spaces = max_word - len(aWord)
    aString = ''
    for s in range(spaces):
      aString = aString + " "
    print(aString + aWord)

  qtd = int(input())
  if(qtd == 0):
    break
  print()