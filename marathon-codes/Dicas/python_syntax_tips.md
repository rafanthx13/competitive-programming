##### IF Ternary (python > 2.4)
value_if_true if condition else value_if_false
## Exemplo:
is_nice = True
state = "nice" if is_nice else "not nice"
## Nesse caso: state = "nice"



##### ShortHand Ternary

# >>> True or "Some"
# True
# >>>
# >>> False or "Some"
# 'Some'

### This is helpful in case where you quickly want to check for the output of a function and give a useful message if the output is empty:
### Isso acontece quando na operação relacional com 'or' tiver algum valor tipo string
### Se retornar um valor nao boleano, retornará o primiero na ordem da esquerda para a direita

# Funciona para 

# >>> output = None
# >>> msg = output or "No data returned"
# >>> print(msg)
# No data returned

# x = "Algo" or 5
# print(x)
## Vai rpintar: "Algo" o primeiro valor

####### Handler List

lista = [1,2,3,4,5,6,7]

lista[start_incluindo:end_excluindo]

ou seja

a[3:5] pega os elementos da posicao [3 a 5-1 = 4] ou seja [index3, index4]
# a ideia é [3:5] nesse espaço voce percorre 2 elementos, de 3 -> 4 (1) e de 4-> 5 e apra no 5 (2)
`lista[:b]` => começa do zero e vai ate onde escolher, list[:3] => [index0, index1, index2] (os 3 primeiros)
lista[a:] => começa de onde voce especificou e vai ate o fim, lista[3:] [index3, index4 ..... ]

index negativo:
-> util quando voce nao sabe o tamanho da string

# lembre-se, voce pode usar o index negativo para pegar os elementos lendo da direita para esquerda:
# lista[-1] => retorna o ultimo elemento da lista
# lista[-3] => retorna o anti-énultimo elmeento da lista

# Lembre-se, lista em python é por referencia, se você faz que lsita1 = lista, as duas estao apaontando para a mesma lista, par aum mesmo objeto
# se voce quer que sejam uma copia, fce pode copiar elementos por elemento ou fazer: lista1 = list(lista) ou lista1 = lista[:] (retorna tudo)


# Passar uma tupla como argumento
https://stackoverflow.com/questions/1993727/expanding-tuples-into-arguments
Basta usar * na variavel da tupla

# Variavel Global
https://www.geeksforgeeks.org/global-keyword-in-python/
Precisar colocar "global variabel_name" caso você for modificala
Agora, se você so vai acessar, nao precisa

Ver o exempl de 1905, nele precisou do global para acessar "flag_win" mas nao precisou para matrix,  jaque agente so acessava o valor
