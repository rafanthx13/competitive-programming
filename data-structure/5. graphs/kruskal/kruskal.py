# Baseado no algoritmo do link a seguir:
# https://www.geeksforgeeks.org/union-find/
# https://www.geeksforgeeks.org/union-find-algorithm-set-2-union-by-rank/

# grafo ponderado com id:int [ [[1,2],[2,4]], [0,2]]
# Por o id ser número, podemos usar o index da lista, asism não precisa ser dict
# o nó 0 aponta para 1 # o nó 0 aponta para 2
# o nó 1 aponta para 2 # O nó 1 aponta para 4

class Grafo:

    def __init__(self, qtd_vertices):
        self.V = qtd_vertices
        self.grafo = []
        # Criação de Vértices : coloca n listas vazias de acordo com o index
        for _ in range(qtd_vertices):
            self.grafo.append([])

    def add_aresta(self, vertice1, vertice2, valor):
        self.grafo[vertice1].append((vertice2, valor))

    # find_parent_optimized() : vai retornar o mais profundo pai do index 'node'
    # no array_parent, vai ser recursivo até encontrar o ultimo que aponta
    def find_parent_optimized(self, array_parent, node):
        # find with path compression
        # Se seu parent for diferente de si mesmo,
        #   entâo vai mudalo, e so depois envialo
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

    # converte de [ [[1,2],[2,3]]] para [ [0,1,2], [0,2,3]]
    def descompact_list(self, alist, size):
        return_list = []
        print("alist", alist)
        for i in range(size):
            for el in alist[i]:
                return_list.append( [i, el[0], el[1]] )
        return return_list

    # Retorna uma liita de [(v1,v2,valor)] das arestas que compoe a MST
    def kruskal(self):

        MST = []

        ### Alterando a lsita para podermos manipuláá melhor
        alist = [x for x in self.grafo]
        # Altera a lista para um formato melhor
        deszip_list = self.descompact_list(self.grafo, self.V)
        # Ordena pelo valor
        edges_sorted = sorted(deszip_list, key = lambda item: item[2])
        # Temos então uma lista de arestas ordenadas por valor
        print(edges_sorted)

        array_parent = [-1]*(self.V)
        array_rank   = [0]*(self.V)

        print("Grafo:\n", "index:      ", [i for i in range(self.V)],
                "\n", "aponta para:", self.grafo, "\n")

        for i,j,value in edges_sorted:
            x = self.find_parent_optimized(array_parent, i)
            y = self.find_parent_optimized(array_parent, j)
            if(x != y):
                MST.append([i,j,value])
                self.union_by_rank(array_parent,array_rank,x,y)

        return MST

# ---- Execution Kruskal Optimized ---- #

g = Grafo(4)
g.add_aresta(0, 1, 10)
g.add_aresta(0, 2, 6)
g.add_aresta(0, 3, 5)
g.add_aresta(1, 3, 15)
g.add_aresta(2, 3, 4)

list_mst = g.kruskal()
print("MST:", list_mst)
print("Quantidade de Nós distintos:", len(set([x[0] for x in list_mst])))
print("Quantidade de Arestas:", len(list_mst))
print("Peso Total:", sum([x[2] for x in list_mst]))
