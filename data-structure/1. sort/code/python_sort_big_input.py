#### BENCHMARK - PYTHON STAND SORT - BIG INPUT ####
import timeit
from statistics import mean

mySetup = """
import timeit
import random

SIZE = 1000000
l = []

for x in range(SIZE):
  l.append( random.randint(0,9999999) )

"""

tempo = timeit.repeat(setup= mySetup, stmt = "l.sort()", repeat=3, number=1)
print('Exec Time: {:.5f} seconds'.format(mean(tempo)))
