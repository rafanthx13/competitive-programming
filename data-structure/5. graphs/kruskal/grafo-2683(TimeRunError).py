# URI 2173 - Grafos - Outubro de 2019
# Assunto: Grafos, MST, Kruskal
# TimeRunError

# Solução: Aplicar Kruskal em uma lsita ordenada e depois
# invertida, para se obter a MST max e min

class Grafo:

    def __init__(self, qtd_vertices):
        self.V = qtd_vertices
        self.grafo = []

    def add_aresta(self, vertice1, vertice2, valor):
        self.grafo.append((vertice1, vertice2, valor))

    def find_parent_optimized(self, array_parent, node):
        if(array_parent[node] == -1):
            return node
        if(array_parent[node] != node):
            array_parent[node] = self.find_parent_optimized(array_parent, array_parent[node])
        return array_parent[node]

    # union_by_rank() : Vai juntar dois subconjuntos
    def union_by_rank(self, array_parent, array_rank, x, y):
        if(array_rank[x] > array_rank[y]):
            array_parent[y] = x
        elif(array_rank[x] < array_rank[y]):
            array_parent[x] = y
        else:
            array_parent[x] = y
            array_rank[y] += 1

    def kruskal_min(self):
        MST = 0
        edges_sorted = self.grafo
        array_parent = [-1]*(self.V)
        array_rank   = [0]*(self.V)
        for i,j,value in edges_sorted:
            x = self.find_parent_optimized(array_parent, i)
            y = self.find_parent_optimized(array_parent, j)
            if(x != y):
                MST += value
                self.union_by_rank(array_parent,array_rank,x,y)
        return MST

    def kruskal_max(self):
        MST = 0
        edges_sorted = self.grafo
        array_parent = [-1]*(self.V + 1)
        array_rank   = [0]*(self.V + 1)
        for i,j,value in edges_sorted[::-1]:
            x = self.find_parent_optimized(array_parent, i)
            y = self.find_parent_optimized(array_parent, j)
            if(x != y):
                MST += value
                self.union_by_rank(array_parent,array_rank,x,y)

        return MST

# Exec

while(True):
  try:
      n = int(input())
      g = Grafo(0)
      vert_max = -1 # qual o vamior valor de um vertice
      for _ in range(n):
          v1, v2, v = list(map(int, input().split()))
          g.add_aresta(v1,v2,v)
          vert_max = max(vert_max, max(v1, v2))
      g.V = vert_max + 1
      g.grafo = sorted(g.grafo, key = lambda item: item[2])
      print(g.kruskal_max())
      print(g.kruskal_min())
  except EOFError:
    break
