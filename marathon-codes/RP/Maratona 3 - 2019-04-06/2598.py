# 2598 - Colocando Radares

import math

times = int(input())
final_list = []

for i in range(times):
    blist = input().split()
    alist = []
    for l in blist:
        alist.append( int(l))
    final_list.append( math.ceil(alist[0] / alist[1]))
    #print( int(alist[0] / alist[1]) + 1)

for x in final_list:
    print(x)
