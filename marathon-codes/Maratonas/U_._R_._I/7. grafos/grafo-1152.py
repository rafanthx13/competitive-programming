# U_R_I - 1155 URI ,UVA 11631 - 7. Grafos - Agosto de 2019 - Assunto: Grafos, MST, Kruskal

# Nestes dias se pensa muito em economia, mesmo em Byteland. Para reduzir custos
# operacionais, o governo de Byteland decidiu otimizar a iluminação das estradas.
# Até agora, todas as rotas eram iluminadas durante toda noite, o que custava 1
# Dólar Byteland por metro a cada dia. Para economizar, eles decidiram não iluminar
# mais todas as estradas e desligar a iluminação de algumas delas. Para ter certeza
# que os habitantes de Byteland continuem a se sentirem seguros, eles querem
# otimizar o sistema de tal forma que após desligar a iluminação de algumas
# estradas à noite, sempre existirá algum caminho iluminado de qualquer junção
# de Byteland para qualquer outra junção.

# Qual é a quantidade máxima de dinheiro que o governo de Byteland pode
# economizar, sem fazer os seus habitantes sentirem-se inseguros?

#       Entrada
# A entrada contém vários casos de teste. Cada caso de teste inicia com
# dois números m (1 ≤ m ≤ 200000) e n (m-1 ≤ n ≤ 200000), que são o número de
# junções de Byteland e o número de estradas em Byteland, respectivamente.
# Seguem n conjuntos de três valores inteiros, x, y e z, especificando qual
# será a estrada bidirecional entre x e y com z metros (0 ≤ x, y < m e x ≠ y).

# A entrada termina com m=n=0. O grafo especificado em cada caso de teste é
# conectado. O tamanho total de todas as estradas em cada caso de teste é
# menor do que 231.

#       Saída
# Para cada caso de teste imprima uma linha contendo a máxima quantidade
# diária de dólares de Byteland que o governo pode economizar.

# Exemplo de Entrada	Exemplo de Saída

# 7 11                51
# 0 1 7
# 0 3 5
# 1 2 8
# 1 3 9
# 1 4 7
# 2 4 5
# 3 4 15
# 3 5 6
# 4 5 8
# 4 6 9
# 5 6 11

## Descriçâo do Problema
# Solução: Aplicar o Kruskal para encontrar a MST a árvore mínima geradora do grafo
# Encontrar seu custo e subtrarir: custo_total (todos os vertices) - custo da MST

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


    # Retorna uma liita de [(v1,v2,valor)] das arestas que compoe a MST
    def kruskal(self):

        MST = []
        edges_sorted = sorted(self.grafo, key = lambda item: item[2])
        array_parent = [-1]*(self.V)
        array_rank   = [0]*(self.V)

        for i,j,value in edges_sorted:
            x = self.find_parent_optimized(array_parent, i)
            y = self.find_parent_optimized(array_parent, j)
            if(x != y):
                MST.append([i,j,value])
                self.union_by_rank(array_parent,array_rank,x,y)

        return MST

while(True):
    vertices, arestas = list(map(int, input().split()))

    if(arestas == 0 and vertices == 0):
        break

    g = Grafo(vertices)
    custo_total = 0
    for _ in range(arestas):
        v1, v2, v = list(map(int, input().split()))
        g.add_aresta(v1, v2, v)
        custo_total += v

    list_mst = g.kruskal()
    print(custo_total - sum([x[2] for x in list_mst]))
