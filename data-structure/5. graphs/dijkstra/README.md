# djisktra

É UM ALGORITMO GULOSO

### Pseudo código

````
1  function Dijkstra(Graph, source):
 2
 3      create vertex set Q
 4
 5      for each vertex v in Graph:             
 6          dist[v] ← INFINITY                  
 7          prev[v] ← UNDEFINED                 
 8          add v to Q                      
10      dist[source] ← 0                        
11      
12      while Q is not empty:
13          u ← vertex in Q with min dist[u]    
14                                              
15          remove u from Q
16          
17          for each neighbor v of u:           // only v that are still in Q
18              alt ← dist[u] + length(u, v)
19              if alt < dist[v]:               
20                  dist[v] ← alt
21                  prev[v] ← u
22
23      return dist[], prev[]
````

> https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

````
1  S ← empty sequence
2  u ← target
3  if prev[u] is defined or u = source: // Do something only if the vertex is reachable
4      while u is defined:            // Construct the shortest path with a stack S
5          insert u at the beginning of S    // Push the vertex onto the stack
6          u ← prev[u]                    // Traverse from target to source
````

## Pra que serve

+ Achar o caminho de menor entre um vértice e todos os outros vértices de um grafo ponderado
+ Gera a  Shortest Path Tree (SPT) [Árvore de Menor caminho] par aum vértice, ou seja, uma árvore do menor caminho entre o vértice escolhido e todos os outros
+ Para saber o caminho entre dois vertices, tem que acumular como em Prim
+ OBS: Não trabalha bem com peso negativo, para isso, usa-se Bellman-Ford


**Complexidade**

O(V^2) para matriz de adjascência
O(ElogV) O(E log V) with the help of binary heap.

**Comentários**

> https://pt.wikipedia.org/wiki/Algoritmo_de_Dijkstra

O algoritmo de Dijkstra não consegue encontrar o menor caminho em um grafo com pesos negativos. Para esse propósito, pode-se usar o algoritmo de Floyd-Warshall, que consegue descobrir a menor distância entre todos os pares de vértices de qualquer grafo sem ciclos com peso negativo em uma complexidade de tempo O(V³). Se o problema não exigir o cálculo da distância entre todos os pares de vértices ou se existirem ciclos com peso negativo, pode-se aplicar o algoritmo de Bellman-Ford, com complexidade de tempo O(V*E). Em uma árvore, é possível encontrar a distância entre um vértice inicial e todos os outros vértices em tempo O(V+E), utilizando busca em profundidade (também conhecida como DFS). Em um grafo cujas arestas têm todas o mesmo peso, pode-se encontrar a distância entre um vértice inicial e todos os outros vértices, para um grafo qualquer, em O(V+E), utilizando busca em largura (também conhecida como BFS). O processo utilizado no algoritmo de Dijkstra é bastante similar ao processo usado no algoritmo de Prim. O propósito deste último, entretanto, é encontrar a árvore geradora mínima que conecta todos os nós de um grafo. O BFS pode ser visto como um caso especial do algoritmo de Dijkstra em grafos não dirigidos, onde a fila de prioridade assume o comportamento FIFO.


## Como funciona

> https://pt.wikipedia.org/wiki/Algoritmo_de_Dijkstra#/media/Ficheiro:Dijkstra_Animation.gif

A ideia é:
+ Crio um array para representar a distancia entre `origin` e todos os outros
 vértices
+ A medida passo peloa vértices e olho as arestas, eu vou vendo as distâncias dos vértices
+ Se `origin = A`, eu tiver `A -> B : 10`, se aparecer um caminho melhor, vou substituir



## Análise passo a passo






|      | v0       | v1       | v2        | v3        | v4   | v5        | v6       | v7       | v8        |
| ---- | -------- | -------- | --------- | --------- | ---- | --------- | -------- | -------- | --------- |
| v0   | <u>0</u> | 4*       |           |           |      |           |          | 8        |           |
| v1   | <u>0</u> | <u>4</u> | 12        |           |      |           |          | 8*       |           |
| v7   | <u>0</u> | <u>4</u> | 12        |           |      |           | 9*       | <u>8</u> | 15        |
| v6   | <u>0</u> | <u>4</u> | 12        |           |      | 11*       | <u>9</u> | <u>8</u> | 15        |
| v5   | <u>0</u> | <u>4</u> | 12*       | 25        | 21   | <u>11</u> | <u>9</u> | <u>8</u> | 15        |
| v2   | <u>0</u> | <u>4</u> | <u>12</u> | **19**    | 21   | <u>11</u> | <u>9</u> | <u>8</u> | **14***   |
| v8   | <u>0</u> | <u>4</u> | <u>12</u> | 19*       | 21   | <u>11</u> | <u>9</u> | <u>8</u> | <u>14</u> |
| v3   | <u>0</u> | <u>4</u> | <u>12</u> | <u>19</u> | 21   | <u>11</u> | <u>9</u> | <u>8</u> | <u>14</u> |
| v4   | <u>0</u> | <u>4</u> | <u>12</u> | <u>19</u> | 21*  | <u>11</u> | <u>9</u> | <u>8</u> | <u>14</u> |

Em v2: houve duas mudanças de `dist`

Sublinhado: Já foi acessado `sptSet[u] = True`

Asterisco (*): O escolhido com menor dist que não esteja em `sptSet`



