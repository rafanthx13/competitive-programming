# https://www.geeksforgeeks.org/timeit-python-examples/

# selection_sort:
## Comesa do Inicio
## Encontrar o menor elemento do array (percorrendo ate o fim) e colocar na 1 posisao
## Avansa 1
## Encontrar o menor e e colcoar na posisao 2 (comesa da 2 posisao agora)
## Faz ate chegar ao final
## Ultra ineficiente

import random
import timeit
from statistics import mean

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

selection_sort(l, SIZE)
print(l)

#### BENCHMARK ####

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

tempo = timeit.repeat(setup= mySetup, stmt = "selection_sort(l, SIZE)", repeat=10, number=1)
print('Exec Time: {:.5f} seconds'.format(mean(tempo)))
