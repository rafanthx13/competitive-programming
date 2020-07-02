## Gerar números `random`
import random

l = []

for x in range(1000):
  l.append( random.randint(0,9999) )


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

