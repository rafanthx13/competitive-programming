# Rafael encontrou um novo hobbie: fazer desenhos usando caracteres do teclado. 
# Por mais simples ou limitada que essa nova forma de arte possa parecer, 
# basta criatividade para se fazer os mais diferentes tipos de desenhos.

# Após fazer alguns desenhos, Rafael imaginou como seriam se eles fossem 
# redimensionados, porém ter que refazer todo o desenho pareceu meio cansativo.
# Para isso, Rafael pediu sua ajuda.

# Em um redimensionamento, uma imagem com N linhas e M colunas passa a ter A 
# linhas e B colunas, e, dado que as novas dimensões da imagem redimensionada 
# é maior do que as dimensões da imagem original, alguns caracteres terão que 
# se repetir.

# Digamos que A seja 3 vezes maior que N. Nesse caso, cada linha terá que se 
# repetir 3 vezes, para que a imagem seja redimensionada de forma correta.

# Dado um desenho feito por Rafael, imprima como seria se o desenho fosse 
# redimensionado para uma determinada nova dimensão.

# Entrada

  # Haverá diversos casos de teste. Cada caso de teste inicia com 
  # dois inteiros N e M (1 ≤ N, M ≤ 50), representando, respectivamente, 
  # a altura e a largura do desenho de Rafael.

  # A seguir haverá N linhas, contendo M caracteres cada, representando o desenho
  # feito por Rafael. Após, haverá dois inteiros A e B (N < A ≤ 100, M < B ≤ 100,
  # A é múltiplo de N, e B é multiplo de M), representando, respectivamente, a 
  # nova altura e largura que Rafael deseja que seu desenho tenha.

  # O último caso de teste é indicado quando N = M = 0, o qual não deverá ser 
  # processado.

# Saída

  # Para cada caso de teste, imprima A linhas, contendo B caracteres cada, 
  # representando o desenho de Rafael redimensionado.

  # Após cada caso de teste, imprima uma linha em branco.

# Exemplo de Entrada	Exemplo de Saída

# 3 3
# ###
# #__
# ###
# 6 9
# 0 0

# #########
# #########
# ###______
# ###______
# #########
# #########

def repeat_letter(l, qtd):
  s = ''
  for _ in range(qtd):
    s = s + l
  return s

def multiply_row(row, scale):
  s = ''
  for l in row:
    s = s + repeat_letter(l,scale)
  return s

def new_row_largura(row, old_m, new_b):
  scale = new_b // old_m
  newlist = []
  for r in row:
    newlist.append(multiply_row(r,scale))
  return newlist

# n/a => qtd de linhas (altura), m/b => qtd de colunas (largura)
while(True):

  n, m = list(map(int, input().split()))
  if(n == 0 and m == 0 ):
    break

  draw = []
  for _ in range(n):
    draw.append(input())

  a, b = list(map(int, input().split()))
  
  aNewList = new_row_largura(draw, m, b) # Largura: Cresce a linha

  # Altura, imprime mais de uma vez
  height_scale = a // n
  for r in aNewList:
    for _ in range(height_scale):
      print(r)

  print()
