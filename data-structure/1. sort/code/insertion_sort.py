# https://www.geeksforgeeks.org/insertion-sort/

import random
import timeit
from statistics import mean

SIZE = 1000
l = []

for x in range(SIZE):
  l.append( random.randint(0,9999) )

def insertion_sort(array, SIZE):
    # Traverse through 1 to len(array)
    for i in range(1, SIZE):

        key = array[i]

        # Move elements of array[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < array[j] :
                array[j + 1] = array[j]
                j -= 1
        array[j + 1] = key


insertion_sort(l, SIZE)
print(l)

#### BENCHMARK ####

mySetup = """
import random
import timeit
from statistics import mean

SIZE = 1000
l = []

for x in range(SIZE):
  l.append( random.randint(0,9999) )

def insertion_sort(array, SIZE):
    # Traverse through 1 to len(array)
    for i in range(1, SIZE):

        key = array[i]

        # Move elements of array[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < array[j] :
                array[j + 1] = array[j]
                j -= 1
        array[j + 1] = key
"""

tempo = timeit.repeat(setup= mySetup, stmt = "insertion_sort(l, SIZE)", repeat=10, number=1)
print('Exec Time: {:.5f} seconds'.format(mean(tempo)))
