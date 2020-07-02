# U_R_I - 1805 - 4. Mat - Agosto de 2019 - Assunto: Progressao Aritmetica (Formula)

# Um número natural é um inteiro não-negativo (0, 1, 2, 3, 4, 5,...). 
# A sua tarefa neste problema é calcular a soma dos números naturais que estão presentes em um determinado intervalo [A, B] inclusive.

# Por exemplo, a soma dos números naturais no intervalo [2, 5] é 14 = (2+3+4+5).

# Entrada
# Cada caso de teste contém dois inteiros A e B (1 ≤ A ≤ B ≤ 10^9), representando o limite inferior e o superior respectivamente.

# Saída
# Para cada caso de teste, a saída consiste de uma linha contendo a soma dos números naturais do intervalo.

# Exemplos

# Entrada        # Saida
# 1 5            # 15
# 1 1000         # 500500
# 10 20          # 165

# Solução: 
# 1. (Ineficiente) Fazer soma por soma
# 2. (Eiciente): Isso é uma P.A (Progressão Aritmetcia) e pra isso tem uma formula
#     Dado uma progressão, onde 
#       a[1] o primeiro termo, 
#       a[n] o ultimo termo
#       n é a n-seima posiçao do termo a[n]
#     Entâo, a formula sera
#       sum = ((a1 + an)*n)/2
#     Temos que descorbir n, que sera NESSE CASO: n = (an - a1) + 1

while(True):
  try:
    a, b = list(map(int, input().split()))
    n = b - a + 1
    r = ((a + b) * n )//2
    print(r)
  except EOFError:
    break