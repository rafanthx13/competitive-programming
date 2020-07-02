# O prefeito de Nlogônia está sendo acusado de usar o asfaltamento como caixa
# dois. Os investigadores suspeitam que ele fez um orçamento maior do que o
# usado nas obras.
#
# Em um pronunciamento oficial, o prefeito disse: “Eu asfaltei o menor
# número de ruas que permitissem aos cidadãos passearem sem precisarem
# passar por uma rua de barro”.
#
# O Folha de Nlogônia conseguiu alguns documentos sobre as ruas que
# poderiam ser pavimentadas e quanto isso custaria. Aqui é onde você
# entra, o jornal te contratou e te forneceu os documentos que eles
# possuem. Então você pode calcular o maior valor que o político pode
#  ter ganho nesse esquema. Lembre-se você deve considerar que o discurso
#  é verdadeiro, caso contrário você pode ser processado.
#
# Entrada
# A entrada contém vários casos de teste. A primeira linha de um caso de
# teste contém dois inteiros N (1 ≤N ≤104) e M(1 ≤M ≤105), o número de
#  esquinas e de ruas respectivamente. Cada uma das próximas M linhas
#  possui três inteiros X (1 ≤X ≤ N), Y(1 ≤ Y ≤ N) e C(1 ≤ C ≤ 103),
#  indicando que para asfaltar a rua que liga a esquina X com a esquina
#   Y o custo é C.
#
# Sempre é possível escolher as ruas de maneira que o discurso do
# prefeito seja verdadeiro.
#
# Depois do último caso de teste, tem uma linha com dois zeros.
#
# Saída
# Para cada caso de teste deve ser impressa uma única linha com um inteiro
#  que representa a maior quantia possível do prefeito roubar e não mentir
#   em seu discurso.
#
# Exemplo de Entrada	Exemplo de Saída
# 3 3                 4
# 1 2 5               6
# 1 3 7
# 2 3 3
# 4 6
# 1 2 1
# 1 3 1
# 1 4 3
# 2 3 3
# 2 4 3
# 3 4 1
# 0 0

# Soluççâo: Caclular a árvore mínima geradora de maior custo e mnor custo
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
