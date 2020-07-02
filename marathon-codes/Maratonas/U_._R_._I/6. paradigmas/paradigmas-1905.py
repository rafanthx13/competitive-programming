# Exemplo de Entrada	Exemplo de Saída
# 2

 
# 0 0 0 0 1
# 1 1 0 0 1
# 0 1 0 0 0
# 0 0 0 1 1
# 1 1 0 0 0
 
# 0 0 0 0 1
# 1 1 0 0 1
# 0 1 0 0 0
# 0 0 1 1 1
# 1 1 0 0 0 
# COPS
# ROBBERS

# (0,0) (0,1) (0,2)
# (1,0) (1,1) (1,2)
# (2,0) (2,1) (2,2)

# Exmeplo HardCode para testar:
# # matrix = [[0, 0, 0, 0, 1], [1, 1, 0, 0, 1], [0, 1, 0, 0, 0], [0, 0, 0, 1, 1], [1, 1, 0, 0, 0]]

# Como resolver: buscar em profundidade marcando o que ja foi visitado
# OBS: a parte do temp é que as vezes entra uma string invalida, como relatado no seguinte link:
# https://www.urionlinejudge.com.br/judge/pt/questions/view/1905/2572

flag_win = False
visited = []

def valid_node(x,y):
  # print("valid", x, y, x >= 0, x <= 5, y >= )
  return x >= 0 and x <= 4 and y >= 0 and y <= 4

# recursao na busca
def search_node(x, y):
  global flag_win
  
  # se encontrou, para
  if(x == 4 and y == 4):
    flag_win = True
    return
  
  # foi visitado
  visited.append((x,y)) 

  # Andar na horizontal é no y
  # Andar na Vertical é no x

  # baixo
  if(valid_node(x+1,y) and matrix[x+1][y] == 0 and (x+1,y) not in visited  ):
    search_node(x+1, y)
  # cima
  if(valid_node(x-1,y) and matrix[x-1][y] == 0 and (x-1,y) not in visited  ):
    search_node(x-1, y)
  # direita
  if(valid_node(x,y+1) and matrix[x][y+1] == 0 and (x,y+1) not in visited  ):
    search_node(x, y+1)
  # esquerda
  if(valid_node(x,y-1) and matrix[x][y-1] == 0 and (x,y-1) not in visited  ):
    search_node(x, y-1)
  

n = int(input())

for _ in range(n):
    # inicializar
    matrix = []
    flag_win = False
    visited = []

    # inserir dados
    for _ in range(5):
      temp = input().split()
      while(not temp):
        temp = input().split()
      if(temp):
        matrix.append(list(map(int, temp)))

    # Buscar do inicio: recursiva
    search_node(0,0) 

    if(flag_win):
      print("COPS")
    else:
      print("ROBBERS")
