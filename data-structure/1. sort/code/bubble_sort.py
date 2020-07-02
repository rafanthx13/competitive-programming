import random
import timeit
from statistics import mean

SIZE = 1000
l = []

for x in range(SIZE):
  l.append( random.randint(0,9999) )

def bubble_sort(array, size):

    # Traverse through all array elements
    for i in range(size):

        # Last i elements are already in place
        for j in range(0, size-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if array[j] > array[j+1] :
                array[j], array[j+1] = array[j+1], array[j]

bubble_sort(l, SIZE)
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

def bubble_sort(array, size):

    # Traverse through all array elements
    for i in range(size):

        # Last i elements are already in place
        for j in range(0, size-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if array[j] > array[j+1] :
                array[j], array[j+1] = array[j+1], array[j]

"""

tempo = timeit.repeat(setup= mySetup, stmt = "bubble_sort(l, SIZE)", repeat=10, number=1)
print('Exec Time: {:.5f} seconds'.format(mean(tempo)))
