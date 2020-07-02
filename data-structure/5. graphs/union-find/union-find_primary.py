# Baseado no algoritmo do link a seguir:
# https://www.geeksforgeeks.org/union-find/

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

    # find_parent() : vai retornar o mais profundo pai do index 'node'
    # no array_parent, vai ser recursivo até encontrar o ultimo que aponta
    def find_parent(self, array_parent, node):
        # se -1: então ele nao esta em nenhum subconjunto, entao ele eh parent de si mesmo
        if(array_parent[node] == -1):
            return node
        else:
            # se nao for -1, entao ele aponta pra alguem
            # voce tem que descobrir esse pai desse alguem
            # o pai de array_parent[node]
            return self.find_parent(array_parent, array_parent[node])

    # union_sets() : o pai de x (ou sele mesmo se for -1)
    # vai apontar para o pai de y
    def union_sets(self, array_parent, x, y):
        x_set = self.find_parent(array_parent, x)
        y_set = self.find_parent(array_parent, y)
        array_parent[x_set] = y_set

    # detecção de ciclo
    # juntar os nós que estejam ligados entre si num mesmo conjunto
    # se ao fazer isso achar um nó que já está no conjunto, então
    # identificou um ciclo
    def cycle_detection(self):

        array_parent = [-1]*(self.V)

        print("Grafo:\n", "index:      ", [i for i in range(self.V)],
                "\n", "aponta para:", self.grafo, "\n")

        for i in range(self.V):
            for j in self.grafo[i]:
                print("Analisando:", i,"=>",j)
                # (i,j) :: areta de i => j
                x = self.find_parent(array_parent, i)
                print("i:", i, "tem como pai:", x)
                y = self.find_parent(array_parent, j)
                print("j:", j, "tem como pai:", y)
                if(x == y):
                    return True
                self.union_sets(array_parent,x,y)
                print("=> array_parent:", array_parent, "\n")
        return False

# ---- Execution ---- #

g = Grafo(3)

g.add_aresta(0, 1)
g.add_aresta(1, 2)
g.add_aresta(2, 0)

if(g.cycle_detection()):
    print("\n==> Graph contains cycle")
else:
    print("\n==> Graph does not contain cycle")
