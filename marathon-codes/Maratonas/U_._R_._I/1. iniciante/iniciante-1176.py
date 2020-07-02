# 1145 - Fibonacci em Vetor

# Exemplo de Entrada	
# 3
# 0
# 4
# 2

# Exemplo de Saída
# Fib(0) = 0
# Fib(4) = 3
# Fib(2) = 1

vetor_fibonacci = {}
vetor_fibonacci[0] = 0
vetor_fibonacci[1] = 1

def fib_top_down(f):
  if(f in vetor_fibonacci):
    return vetor_fibonacci[f]
  else:
    vetor_fibonacci[f] = fib_top_down(f-1) + fib_top_down(f-2)
    return vetor_fibonacci[f]

n = int(input())
lista = []

for i in range(n):
  q = int(input())
  lista.append( (q, fib_top_down(q)) )

for j in lista:
  print("Fib(" + str(j[0]) + ") = " + str(j[1]) )