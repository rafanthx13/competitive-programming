listaA = input().split()
listaB = []

for i in range(int(listaA[0])):
    listaAUX = input().split()
    
    if(i % 2 != 0):
        listaAUX.reverse()

    listaB += listaAUX

for i in listaB:
    print(str(i) + ' ', end = '')
print()