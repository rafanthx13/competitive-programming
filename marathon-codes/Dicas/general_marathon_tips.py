##### Iterar um dicionario
aDict = { 'key1' : 4}
##### Iterar chave e valor
for (key, value) in aDict.items():
    print(key, value)
##### Iterar por valor
for value in aDict.values():
    print(value)
##### Iterar por chave
for key in aDict.keys():
    print(key)

##### Ler numa linha uma lista de inteiros separados por ' '
list_int = list(map(int, input().split()))

##### Programação Dinâmica e Recursão
vetor_fibonacci = {}
vetor_fibonacci[0] = 0
vetor_fibonacci[1] = 1

def fib_top_down(f):
  if(f in vetor_fibonacci):
    return vetor_fibonacci[f]
  else:
    vetor_fibonacci[f] = fib_top_down(f-1) + fib_top_down(f-2)
    return vetor_fibonacci[f]

##### EOF Error template
while(True):
    try:
        x = input().split()
        l.append(x)
    except EOFError:
        break

#####dict.setdefault

# Sintaxe
dict.setdefault(key, default = None) # equivalente ha: dict[key] = default 
# So cria essa nova chave SE ELA NAO EXISTIR, SE JÁ EXISTIR, NÂO MUDA NADA


####

while(True):
  try:
    pass
  except EOFError:
    break

