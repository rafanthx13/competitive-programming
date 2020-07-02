import random
import timeit
from statistics import mean

SIZE = 1000
l = []

for x in range(SIZE):
  l.append( random.randint(0,9999) )

l.sort()
print(l)

#### BENCHMARK ####

mySetup = """
import timeit
import random

SIZE = 1000
l = []

for x in range(SIZE):
  l.append( random.randint(0,9999) )

"""

tempo = timeit.repeat(setup= mySetup, stmt = "l.sort()", repeat=10, number=1)
print('Exec Time: {:.5f} seconds'.format(mean(tempo)))
