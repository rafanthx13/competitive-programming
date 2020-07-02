#  URI - 1764  7. Grafos - Outubro de 2019 - Assunto: Grafos, MST, Kruskal
#
# Antes de Papai Noel começar a fazer as suas viagens de trenó pelo Brasil para
# entregar os presentes de Natal, ele solicitou que você o ajudasse a desenhar
# um mapa com todas as cidades que deverá visitar. A regra para desenhar este
# mapa é a seguinte: a soma de todas rotas (distâncias entre duas cidades)
# existentes no mapa deve ser a menor possível e deve-se poder chegar em
# qualquer cidade, independente de onde se esteja partindo. Noel não se importa
# de passar por uma determinada cidade mais de uma vez, contanto que ele
# utilize apenas as rotas desenhadas no mapa.
#
# Entrada
# A entrada contém vários casos de teste. A primeira linha de cada caso de teste
#  contém dois inteiros, M (2 ≤ M < 40000) e N (1 ≤ N < 50000), que indicam
#  respectivamente a quantidade de cidades e a quantidade de caminhos existentes
#   ligando estas cidades. A entrada é terminada por M = N = 0. Seguem N
#   conjuntos de três valores X (0 ≤ X), Y (Y < M) e Z (1 ≤ Z ≤ 999),
#   especificando que há uma rota bidirecional entre X e Y com distância
#   de Z kilômetros, sendo que X ≠ Ye a soma total de todas as rotas de cada
#    mapa é menor do que 231.
#
# Saída
# Para cada caso de teste de entrada, seu programa deverá imprimir um único
# valor, indicando a soma de todas as distâncias ou rotas existentes no seu mapa.

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


    # Retorna uma lista de [(v1,v2,valor)] das arestas que compoe a MST
    def kruskal(self):

        MST = 0
        edges_sorted = sorted(self.grafo, key = lambda item: item[2])
        array_parent = [-1]*(self.V)
        array_rank   = [0]*(self.V)

        for i,j,value in edges_sorted:
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

    g = Grafo(vertices)
    for _ in range(arestas):
        v1, v2, v = list(map(int, input().split()))
        g.add_aresta(v1, v2, v)

    print(g.kruskal())
