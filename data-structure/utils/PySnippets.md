-----------------------------------------------------------------------

## Gerar números `random`
import random

l = []

for x in range(1000):
  l.append( random.randint(0,9999) )

-----------------------------------------------------------------------

## Calcular tempo de uma função
mySetup = """
import random
import timeit

SIZE = 1000
l = []

for x in range(SIZE):
  l.append( random.randint(0,9999) )

def selection_sort(array, size):
    # Percorrer n vezes
    for i in range(size):
        min_index = i
        # Percorer n - i vezes
        for j in range(i+1, size):
            if(array[min_index] > array[j]):
                min_index= j
        # swap
        array[i], array[min_index] = array[min_index], array[i]
"""

# Vai executar 10 vezes
tempo = timeit.repeat(setup= mySetup, stmt = "selection_sort(l, SIZE)", repeat=10, number=1)
# A saida sera a media das 10 execuçôes, formatado em 5 casa decimais
print('Exec Time: {:.5f} s'.format(mean(tempo)))


-----------------------------------------------------------------------

## Para testar entradas raw 
string_pessoas = """
Capheus 1
Nomi 8
Lito 1
Will 1
Kala 1
Wolfgang 1
Sun 1
Riley 1
Abner 5
""".split("\n")[1:-1]

RETORNA

['Capheus 1', 'Nomi 8', 'Lito 1', 'Will 1', 'Kala 1', 'Wolfgang 1', 'Sun 1', 'Riley 1', 'Abner 5']

-----------------------------------------------------------------------

while(True):
  try:
    pass
  except EOFError:
    break

-----------------------------------------------------------------------

# URI 1155, UVA 11631 - Grafos - Outubro de 2019
# Assunto: Grafos, MST, Kruskal
# Accepted

## Solução
# Aplicar o Kruskal para encontrar a MST a árvore mínima geradora do grafo
# Encontrar seu custo e subtrarir:
#   custo_total (todos os vertices) - custo da MST

-----------------------------------------------------------------------

