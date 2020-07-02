# Crie um programa para ordenar um conjunto de strings pelo seu tamanho.
#  Seu programa deve receber um conjunto de strings e retornar este mesmo 
# conjunto ordenado pelo tamanho das palavras, se o tamanho das strings for
#  igual, deve-se manter a ordem original do conjunto.

# Entrada
# A primeira linha da entrada possui um único inteiro N, que indica o número
#  de casos de teste. Cada caso de teste poderá conter de 1 a 50 strings
#  inclusive, e cada uma das strings poderá conter entre 1 e 50 caracteres 
# inclusive. Os caracteres poderão ser espaços, letras, ou números.

# Saída
# A saída deve conter o conjunto de strings da entrada ordenado pelo tamanho
#  das strings. Um espaço em branco deve ser impresso entre duas palavras.

# Exemplo de Entrada	Exemplo de Saída
  # 4
  # Top Coder comp Wedn at midnight
  # one three five
  # I love Cpp
  # sj a sa df r e w f d s a v c x z sd fd

  # midnight Coder comp Wedn Top at
  # three five one
  # love Cpp I
  # sj sa df sd fd a r e w f d s a v c x z

n = int(input())
 
for q in range(n):

  s = input().split()

  h = {}

  for w in s:
    l = len(w)
    if(l not in h):
      h[l] = []
      h[l].append(w)
    else:
      h[l].append(w)

  sorteds_keys = sorted(h.keys())

  for ord_key in sorteds_keys[::-1]:
    aList = h[ord_key]
    for i in aList:
      # if(i == h[sorteds_keys[0]][0]):
      #   print(i, end = "")
      # else:
      print(i, end = " ")

  if(q != n-1):
    print()