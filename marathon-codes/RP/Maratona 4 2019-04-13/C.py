inteiro = int(input())

lista = input().split()
listaint = []

listab = input().split()
listabint = []

for i in range(inteiro):
    listaint.append(int(lista[i]))

for i in range(2):
    listabint.append(int(listab[i]))

subvetor = listaint[listabint[0]-1:listabint[1]]
print(max(subvetor) - min(subvetor))