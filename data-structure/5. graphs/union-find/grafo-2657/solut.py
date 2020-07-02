# dic = {}
# sz = [0]*10001
# iid = [0]*10001
#
# def find(x):
#   if(iid[x] == x):
#     return x
#   return find(iid[x])
#
# def union(p, q):
#   p = find(p)
#   q = find(q)
#   if(p == q):
#     return
#   if(sz[p] > sz[q]):
#     aux = p
#     p = q
#     q = aux
#   iid[p] = q
#   sz[q] += sz[p]
#   sz[p] = sz[q]
#
# n, m, q = map(int,input().split())
# cont = 0
# lvl = [0]*n
#
# for i in range(n):
#   a, b = input().split()
#   dic[a] = cont
#   iid[i] = i
#   cont+=1
#   sz[i] = 1
#   lvl[i] = int(b)
#
# for i in range(m):
#   x, y = input().split()
#   union(dic[x], dic[y])
#
# for i in range(q):
#   x = input()
#   if sz[dic[x]] < 2:
#     print("S")
#   else:
#     if lvl[dic[x]] >= 5:
#       print("S")
#     else:
#       k = find(dic[x])
#       estado = 1
#       for j in range(n):
#         m = find(j)
#         if m == k:
#           if lvl[j] > 5:
#             estado = 0
#             break
#       if estado == 0:
#         print("N")
#       else:
#         print("S")
