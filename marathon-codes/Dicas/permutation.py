# Link
## https://www.geeksforgeeks.org/permutation-and-combination-in-python/

from itertools import permutations 

# Input  : String ou lista de numeros
# Output : Lista de tuplas

# Obs, se vocÊ fizer len() ou list() no resultado de um 'iterttols' buca muito


# Permutações
## Gera todas as possibildiades dessa string : Gera fatorial(string.length)
## Permut(n) = n!
### Exeplo: Para "ABC" gera 6 possibilidades 3!
string = "ABC"
permut = permutations(string)
print("Permutacao:", string)
for i in permut:
    print(i)
    
    
# Permutações com Repetição
## Gera todas as possibilidades tirando os casos em que haja repetição
##  Funciona quando na entrada há caracteres iguai, se todos forem diferentes, vira a permutação normal
## Permut_Repet(n) = n!/(a!b!c!...) onde a,b,c é a quantidade de vezes que se repete o character
##  Exemplo: "XXYZ" = 4!/(2!1!1!) = 12
### OBs: FOi necessario jogar num set para tirar repetição
count1 = 0
string1 = "XXYZ"
permut_r = permutations(string1)
s = set(list(permut_r))

for j in s:
    count1 = count1 + 1
    
print("Permutacao com repeticao:", string1, "gerou", count1)
    
for j in s:
    print(j)
