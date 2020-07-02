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

    def add_aresta(self, vertice1, vertice2):
        self.grafo[vertice1].append(vertice2)

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

    # detecção de ciclo
    # juntar os nós que estejam ligados entre si num mesmo conjunto
    # se ao fazer isso achar um nó que já está no conjunto, então
    # identificou um ciclo
    def cycle_detection(self):

        array_parent = [-1]*(self.V)
        array_rank   = [0]*(self.V)

        print("Grafo:\n", "index:      ", [i for i in range(self.V)],
                "\n", "aponta para:", self.grafo, "\n")

        for i in range(self.V):
            for j in self.grafo[i]:
                print("Analisando:", i,"=>",j)
                # (i,j) :: areta de i => j
                x = self.find_parent_optimized(array_parent, i)
                print("i:", i, "tem como pai:", x)
                y = self.find_parent_optimized(array_parent, j)
                print("j:", j, "tem como pai:", y)
                if(x == y):
                    return True
                # OBS: você so pode fazer union se (x != y), pois, se fizer
                # union quando (x == y) vai criar um ciclo e vai bugar o find
                self.union_by_rank(array_parent,array_rank,x,y)
                print("=> array_parent:", array_parent, "\n")
        return False

# ---- Execution Kruskal Optimized ---- #

g = Grafo(3)

g.add_aresta(0, 1)
g.add_aresta(1, 2)
g.add_aresta(2, 0)

if(g.cycle_detection()):
    print("\n==> Graph contains cycle")
else:
    print("\n==> Graph does not contain cycle")
