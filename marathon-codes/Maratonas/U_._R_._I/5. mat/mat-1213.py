# Dado qualquer inteiro n (1 ≤ n ≤ 10000) não divisível por 2  ou por 5,
#  algum múltiplo de n deve ser um número que é uma sequência de números 1. 
# Você deve então calcular e mostrar quantos dígitos tem o menor múltiplo de
#  n que tem todos seus dígitos iguais a 1.

# Entrada
# A entrada consiste de vários casos de teste e termina com EOF.
#  Cada caso de teste contém um inteiro n (1 ≤ n ≤ 10000) não divisível por 2 ou por 5.

# Saída
# Para cada caso de teste, imprima quantos dígitos tem o múltiplo de n que atende os requisitos acima.

# Exemplo de Entrada	Exemplo de Saída
# 3
# 7
# 9901

# 3     # pois: 111 % 3 == 0
# 6     # pois: 111111 % 7 == 0
# 12    # pois: 111111111111 % 12 == 0

# Solução: Se não é divisível por 2 e por 5 entâo ele termina em: 1,3,7,9
# Nâo entendi

while(True):
  try:
    n = int(input())
    l = 1
    c = 1
    while(l % n != 0):
      # print("l =", "(10 *", l, "+ 1)", "%", n, "==>", (10 * l + 1), "%", n, "==>\n", "l =", (10 * l + 1) % n)
      l = (10 * l + 1) % n
      c += 1
    print(c)
  except EOFError:
    break


