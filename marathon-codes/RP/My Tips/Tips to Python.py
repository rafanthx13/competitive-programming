# Ler numa linha uma lista de inteiros separados por ' '
list_int = list(map(int, input().split()))

# Exemplo de recursão em fatorial:
def fat(m):
    if (m < 1):
        return 1
    else:
        return m * fat(m-1)

# Iterar um dicionario
aDict = { 'key1' : 4}
## Iterar chave e valor
for (key, value) in aDict.items():
    print(key, value)
## Iterar por valor
for value1 in aDict.values():
    print(value1)
## Iterar por chave
for key1 in aDict.keys():
    print(key1)

# Fatorial com programação Dinâmica
store_fat = {}

def fat(m):
    if (m < 1):
        return 1
    else:
        if(m in store_fat.keys()):
            #print('store', m)
            return store_fat[m]
        else:
            return m * fat(m-1)

def fat_optimized(m):
    if(m in store_fat.keys()):
        return store_fat[m]
    aFat = fat(m)
    store_fat[m] = aFat
    return aFat
