# 1145 - Sequência Lógica 2

# Cada sequência deve ser impressa em uma linha apenas, 
# com 1 espaço em branco entre cada número, conforme 
# exemplo abaixo. Não deve haver espaço em branco após o último valor da linha.

# Exemplo de Entrada	Exemplo de Saída
# 3 99

# 1 2 3
# 4 5 6
# 7 8 9
# 10 11 12
# ...
# 97 98 99

x, y = list(map(int, input().split()))
count = 1
while(True):
  for i in range(x):
    if(count > y):
      break
    if(i == x - 1):
      print(count)
      count = count + 1
      break
    print(str(count) + " ", end="")
    count = count + 1
    
  if(count > y):
      break
