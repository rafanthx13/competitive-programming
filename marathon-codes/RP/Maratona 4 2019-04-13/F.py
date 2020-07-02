n = int(input())
lista = input().split()

soma = 0
partes = 0

for i in range(0, n):
    soma += int(lista[i])

separador = soma/3
soma = 0

for j in lista:
    soma += int(j)
    if (soma == separador):
        soma = 0
        partes += 1


if (partes == 3):
    print('Sim :(')
else:
    print('Nao :)')