# URI 2173 - Grafos - Outubro de 2019
# Assunto: Grafos, MST, Kruskal, Árvore Geradora
# RunTimeError

# Solução: Caclular a árvore mínima geradora de maior custo e mnor custo
# e retornar asism a difereça. A questão pede pra saber quanto é que pode roubar
# Para roubar ele tem que vazer o máximo, e, para não roubar o mínimo
# Então a quantidade que pode roubar é a difenreça entre esses dois valoress

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
            array_parent[node] = self.find_parent_optimized(
                array_parent, array_parent[node])
        return array_parent[node]

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

while(True):
    vertices, arestas = list(map(int, input().split()))

    if(arestas == 0 and vertices == 0):
        break

    g = Grafo(vertices + 2)
    for _ in range(arestas):
        v1, v2, v = list(map(int, input().split()))
        g.add_aresta(v1, v2, v)

    g.grafo = sorted(g.grafo, key = lambda item: item[2])

    print(g.kruskal_max() - g.kruskal_min())
