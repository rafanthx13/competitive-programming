# Disjoint Set

## Links

+ https://www.geeksforgeeks.org/union-find/

## Union-Find

> A *[disjoint-set data structure](http://en.wikipedia.org/wiki/Disjoint-set_data_structure)* is a data structure that keeps track of a set of elements partitioned into a number of disjoint (non-overlapping) subsets

EDA (Estrutura de Dados Abstrata) que suporta duas poerações
+ `find()` : saber se um elemento/subconjuntos esta dentro de outro. Determinanr o subconjunto de um elemetno particular. Se está ou nâo num mesmo subconjunto
+ `union()` : junta dois subconjuntos em  um unico subconjunto

### Pra quer serve

+ Verificar coisas da teoria de conjuntos em estruturas computacionais
+ Detectar se dois elementos estão em um mesmo conjunto

- Operaçôes de grafo:
  - Detectar ciclos em grafo
  - Contar a quantidade de conjuntos dinsjuntos de um grafo (a quantidade de componenstes que nâo se ligam)

###  Cyrcle Detection in graphs
Ideia:

1. Cada vertice começa como um subconjunto
2. Una os conjuntos que são ligados por arestas
3. se acontecer de, ao juntar um conjunto com um elemento, esse elemento
   já pertencer ao conjunto, então, acahamos um ciclo

**Como fazer (`parrent_array`)**

1. Usamos um array (`parrent_array` ) do tamanho da quantiadde de vertices para sinalizar os conjuntos disjuntos. Os elementos são inicializados com -1, onde:

  + index: O index representa o nó
  + valor: Representa o index do nó pai (o subconjunto que pertence)  
    + Ao começar com -1, é como dizer que pertence a a si mesmo, e assim cada elemetno é um subconjunto

  Ele sereve para juntar os conjuntos, exemplo:

  se tivermos `array[1] = 2` então, o elemento 1 está no mesmo subconjunto que o elemento 2.

  **OBS:** O `parent` será o ultimo pai do paii, e asism recursivamente. Dessa forma o algoritmo bai reduzir os n subconjuntos iniciais para a menor quantidade de subconjunto possíveis. Ou seja, ao final **a contagem de -1 do `parent_array` representa a quantidade de conjuntos disjuntos do nosso grafo **

2. Iteramos sobre as arestas : par (vertice1, vertice2)

     + Verificamos os valores de `find(vertice1)` e `find(vertice2)`  ou seja seus pais.
       + Lembrete: o Pai é o ultimo pai até chegar a -1
     + Se o forem diferentes, então, une eles
       + Como estamos olhandos as arestas, sabemos que estao ligadaos, entâo, os unimos
     + Se são iguais, entâo encontramos um ciclo

3. Ao fazer o `union()`, o vertice1 vai receber `parent` devertice2 , formando assim um conjunto
     A ORDEM É `union(menor, maior) => array[menor] = maior`

### Algoritmos em Python

```python
# find_parent() : vai retornar o mais profundo pai do index 'node'
    # no array_parent, vai ser recursivo ate encontrar o ultimo que aponta
    def find_parent(self, array_parent, node):
        # se -1: entap ele nao esta em nenhum ssubconjunto, entao ele eh parent de si mesmo
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
        parent[x_set] = y_set

    # detecçâo de ciclo
    # juntar os nós que estejam ligados entre si num mesmo conjunto
    # se ao fazer isso acahar um nó que já está no conjunto, então
    # identificou um ciclo
    def cycle_detection(self):

        array_parent = [-1]*(self.V)

        for i in range(self.V):
            for j in self.grafo[i]:
                # (i,j) :: areta de i => j
                x = self.find_parent(array_parent, i)
                y = self.find_parent(array_parent, j)
                if(x == y):
                    return True
                self.union(parent,x,y)
        return False
```

## Union-Find Otimizado

https://www.geeksforgeeks.org/union-find-algorithm-union-rank-find-optimized-path-compression/
https://www.geeksforgeeks.org/union-find-algorithm-set-2-union-by-rank/

### Por que fazzer:

1. Nâo é tão difícil
2. Se otimizar, no pior caso, o union-find tem custo linear. Otimizado: tem custo log n

### Otimizaçâo pelo `rank` : `union by rank`

Adicionando um rank aos nós e usando esse ranke para fazer o `union()` podemos evitar formar um encademaneto grande de nós. Assim, quando for aplicar o `find()` vai encontrar mais rápido.

Dados os elementos 0,1,2,3

Sem o rank, no fim do union-find fica:

0 <- 1 <- 2 <- 3

Se colocarmos para quando fazer o union() para apontar para o que tem o maior rank, assim vai ficar:

```
   1    
/  |  \
0   2   3
```

Porque otimiza: Assim, se precisar fazer o find de 0,2,3 vai so dar um salto, enquanto que no anterior dava mais

Como fazer: no Union, quando um for apontar para o outro, coloque para que o menor aponte para o de maior rank. Se os ranks forem iguais, escolha qualquer um deles e aumente mais 1 e aponte o menor para o maior (o que acabou de adicionar)

## Otimizaçâo de compactar de caminho `find with compression path`

Quando for fazer o find() aproveite para encontar o encademento de nós, colocando logo para que o elemento aponte para o último pai encontrado.

Let the subset {0, 1, .. 9} be represented as below and find() is called
for element 3.
              9
         /    |    \  
        4     5      6
     /     \        /  \
    0        3     7    8
            /  \
           1    2  

When find() is called for 3, we traverse up and find 9 as representative
of this subset. With path compression, we also make 3 as the child of 9 so
that when find() is called next time for 1, 2 or 3, the path to root is reduced.

               9
         /    /  \    \
        4    5    6     3
     /           /  \   /  \
    0           7    8  1   2  

### Como fazer

**union by rank**
Para o rank, crie um vetor igual ao `parent_array` agora inicializado com 0. Passe-o  no union e o modifique (isso se a identificaçâo dos nós for por index). 

````python
def union_by_rank(self, array_parent, array_rank, x, y):
        if(array_rank[x] > array_rank[y]):
            array_parent[y] = x
        elif(array_rank[x] < array_rank[y]):
            array_parent[x] = y
        else:
            array_parent[x] = y
            array_rank[y] += 1

````

**find with path compression**

Antes de retornar o valor do fin() de um elemtno, coloque esse elemento apra paontar para esse ultimo find

````python
def find_parent_optimized(self, array_parent, node):
    if(array_parent[node] == -1):
        return node
    if(array_parent[node] != node):
        array_parent[node] = self.find_parent_optimized(
            array_parent, array_parent[node])
    return array_parent[node]
````

**Detecçâo de ciclo**

```python
def cycle_detection(self):

    array_parent = [-1]*(self.V)
    array_rank   = [0]*(self.V)

    for i in range(self.V):
        for j in self.grafo[i]:
            x = self.find_parent_optimized(array_parent, i)
            y = self.find_parent_optimized(array_parent, j)
            if(x == y):
                return True
            self.union_by_rank(array_parent,array_rank,x,y)

    return False
```

