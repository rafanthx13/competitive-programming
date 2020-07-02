# URI - 1466 - Arvore Binaria
class Node:
    def __init__(self, valor, p):
        self.l = None
        self.r = None
        self.v = valor
        self.level = p

    def insert(self, valor):
        if(valor > self.v):
            if(self.r == None):
                self.r = Node(valor, self.level + 1)
            else:
                self.r.insert(valor)
        if(valor < self.v):
            if(self.l == None):
                self.l = Node(valor, self.level + 1)
            else:
                self.l.insert(valor)

    def run(self, lis):
        lis.append((self.v, self.level))
        if(self.l != None):
            self.l.run(lis)
        if(self.r != None):
            self.r.run(lis)
        return lis

def takeSecond(s):
  return s[1]

n = int(input())

for i in range(n):
    nn = int(input())
    lista = list(map(int, input().split()))
    tree =  Node(lista[0], 0)
    for k in range(1, nn):
        tree.insert(lista[k])
    alista = []
    saida = tree.run(alista)
    sortedList = sorted(saida, key=takeSecond)
    r = ''
    for j in sortedList:
      r = r + str(j[0]) + " "
    print("Case " + str(i+1) + ":")
    print(r[:-1])
    print()