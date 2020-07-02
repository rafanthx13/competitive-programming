# U_R_I - 5. Mat - Agosto de 2019 - Matemática, divisão e mod

# As crianças são ensinadas a adicionar vários dígitos da direita para 
# a esquerda, um dígito de cada vez. Muitos acham a operação "vai 1" 
# (em inglês chamada de "carry", na qual o valor 1 é carregado de uma 
# posição para ser adicionado ao dígito seguinte) um desafio significativo.
#  Seu trabalho é para contar o número de operações de carry para cada um 
# dos problemas de adição apresentados para que os educadores possam 
# avaliar a sua dificuldade.

# Entrada
#  Cada linha de entrada contém dois inteiros sem sinal com no máximo 9 dígitos.
#  A última linha de entrada contém 0 0.

# Saída
# Para cada linha de entrada, com exceção da última, você deve computar e 
# imprimir a quantidade de operações "leva 1" que resultam da adição dos 
# 2 números, no formato apresentado no exemplo abaixo.

# Exemplos

# Entradas      Saida
# 123 456         No carry operation.
# 555 555         3 carry operations.
# 123 594         1 carry operation.

# 146423 446456   1 carry operation.
# 545655 55578    5 carry operations.
# 146423 594644   3 carry operations.

# 9999 999        4 carry operations.
# 95 94           1 carry operation.
# 1995 95         3 carry operations.

# 0 0

# Solução: 
#     É a soma que fazemos no papel, conte quantos +1 coloca no total
#     OBS: se tiver 4 + 5 e tiver um carry-on antes, ELE CONTA, e faz outro carry on e isso é contado
#     Como resolvi: inverte (começa do fim para o inio do algarimos); determina quantos algarismo é contado
#     Cuidado: depois do limit, pode ter um carry + 9 que pode fazer continuar
#     Faça 99999 + 1 ==> DEve sair 5 carry operations

# s[::-1]

# [c for c in "foobar"] => ['f', 'o', 'o', 'b', 'a', 'r']

while(True):

  a,b = list( input().split() )
  if( a == "0" and b == "0" ):
    break
  
  # inverte string para facilitar, pois podem ter tamanhos diferentes
  a = [int(el) for el in a[::-1]]
  b = [int(el) for el in b[::-1]]
  # teremos uma lista de inteiros  

  # definindo qual deles tem menos algarismos
  if(len(a) < len(b)):
    limit = len(a)
    bigger = b
    len_bigger = len(b)
  else:
    limit = len(b)
    bigger = a
    len_bigger = len(a)

  # Contando carrys
  carry_out = 0
  count = 0
  index = 0
  for i in range(limit):
    r = a[i] + b[i] + carry_out
    
    if(r > 9):
      count += 1
      carry_out = 1
    else:
      carry_out = 0

    index = i
  
  # tem carryon que, se juntar com 9 cria outro
  while(True):
    if(index + 1 < len_bigger): # se tem mais
      index += 1
      if(carry_out == 1 and bigger[index] == 9):
        
        rr = carry_out + bigger[index]

        if(r > 9):
          count += 1
          carry_out = 1
        else:
          carry_out = 0

      else:
        break
    else:
      break
  
  # resultado
  if(count == 0):
    print("No carry operation.")
  else:
    if(count == 1):
      print("1 carry operation.")
    else:
      print(count, "carry operations.")