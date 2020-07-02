import random
import timeit
from statistics import mean

SIZE = 1000
l = []

for x in range(SIZE):
  l.append( random.randint(0,9999) )


def partition(arr,low,high):
    i = ( low-1 )         # index of smaller element
    pivot = arr[high]     # pivot

    for j in range(low , high):

        # If current element is smaller than the pivot
        if   arr[j] < pivot:

            # increment index of smaller element
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]

    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )

# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort
def quick_sort(arr,low,high):
    if low < high:

        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr,low,high)

        # Separately sort elements before
        # partition and after partition
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)

# Driver code to test above
quick_sort(l,0,SIZE-1)
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


def partition(arr,low,high):
    i = ( low-1 )         # index of smaller element
    pivot = arr[high]     # pivot

    for j in range(low , high):

        # If current element is smaller than the pivot
        if   arr[j] < pivot:

            # increment index of smaller element
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]

    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )

# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort
def quick_sort(arr,low,high):
    if low < high:

        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr,low,high)

        # Separately sort elements before
        # partition and after partition
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)
"""

time = timeit.repeat(setup= mySetup, stmt = "quick_sort(l,0,SIZE-1)", repeat=10, number=1)
print('Exec Time: {:.5f} seconds'.format(mean(time)))
