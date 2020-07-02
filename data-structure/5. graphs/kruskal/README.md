# Kruskal


## Links

+ https://www.ime.usp.br/~pf/algoritmos_para_grafos/aulas/kruskal.html

## kruskal

### O que é Kruskal

Algoritmo de Grafo que resolve o seguinte problema: **Problema:  Encontrar uma MST (árvore geradora de custo mínimo / Minimun Spanning Tree) de um grafo não-dirigido com custos nas arestas.**. Isto significa que ele encontra um subconjunto das arestas que forma uma árvore que inclui todos os vértices, onde o peso total, dado pela soma dos pesos das arestas da árvore, é minimizado. Se o grafo não for conexo, então ele encontra uma floresta geradora mínima (uma árvore geradora mínima para cada componente conexo do grafo). É um algoritmo GULOSO (Greedy)

### Como fazer Kruskal

1. Ordene em ordem crescente as arestas pelos pesos
2. Crie um vetor/EAD para armazenar a arvore minima geradora que começa como vazia (MST)
3. for each aresta (em ordem crescente de peso):
4.   Adiciona a aresta a MST se nâo forma ciclo

É um algortimo gulos por ja buscar colocar o mneor vlaor possível

**Na Prática**
1. Inicialize a lista de retorno (MST)
2. Ordene as arestas em forma crescente de peso
3. Para cada aresta:
4.    Encontre os pais de v1 e v2 (x,y)
5.    Se (x != y)
6.      Então nâo forma ciclo, adiciona na MST e faz union(x,y)

### Algoritmo em python

````python
class Grafo:

    def __init__(self, qtd_vertices):
        self.V = qtd_vertices
        self.grafo = []

    def add_aresta(self, vertice1, vertice2, valor):
        self.grafo[vertice1].append((vertice2, valor))

    def find_parent_optimized(self, array_parent, node):
        if(array_parent[node] == -1):
            return node
        if(array_parent[node] != node):
            array_parent[node] = self.find_parent_optimized(array_parent, array_parent[node])
        return array_parent[node]

    def union_by_rank(self, array_parent, array_rank, x, y):
        if(array_rank[x] > array_rank[y]):
            array_parent[y] = x
        elif(array_rank[x] < array_rank[y]):
            array_parent[x] = y
        else:
            array_parent[x] = y
            array_rank[y] += 1

    def descompact_list(self, alist, size):
        return_list = []
        print("alist", alist)
        for i in range(size):
            for el in alist[i]:
                return_list.append( [i, el[0], el[1]] )
        return return_list

    def kruskal(self):

        MST = []
        edges_sorted = sorted(self.grafo, key = lambda item: item[2])

        array_parent = [-1]*(self.V)
        array_rank   = [0]*(self.V)

        print("Grafo:\n", "index:      ", [i for i in range(self.V)],
                "\n", "aponta para:", self.grafo, "\n")

        for i,j,value in edges_sorted:
            x = self.find_parent_optimized(array_parent, i)
            y = self.find_parent_optimized(array_parent, j)
            if(x != y):
                MST.append([i,j,value])
                # Se somente precisar valor da MST, 
                # subtitua por (int) e va incremento pondo 
                # 'value'. MST += value
                self.union_by_rank(array_parent,array_rank,x,y)

        return MST

# ---- Execution Kruskal ---- #

g = Grafo(4)
g.add_aresta(0, 1, 10)
g.add_aresta(0, 2, 6)
g.add_aresta(0, 3, 5)
g.add_aresta(1, 3, 15)
g.add_aresta(2, 3, 4)

list_mst = g.kruskal() # retorna a lista de tuplas v1,v2,value) da MST
print("MST:", list_mst)
print("Quantidade de Arestas:", len(list_mst))
print("Peso Total da MST:", sum([x[2] for x in list_mst]))
````
