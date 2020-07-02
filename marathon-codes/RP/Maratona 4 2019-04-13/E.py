saida = []

def fat(m):
    if (m < 1):
        return 1
    else:
        return m * fat(m-1)

vetorFat = {}

while True:
    try:
        lista = input().split()
        if (lista == None or lista == []):
            break

        numero = int(lista[0])**int(lista[1])

        i = 1
        while fat(i) % numero != 0:
            i += 1

        i = 1
        while True:
            vectorFat[str(i)] = fat(i)
            if(vectorFat[str(i)] != None):
                aFat = vectorFat[str(i)]
        
        saida.append(i)

    except EOFError:
        break

for i in saida:
    print(i)