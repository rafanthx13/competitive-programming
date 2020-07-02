# Bellman-Ford

**Objetivo**: EM um grafo ponderado, dado um vértice encontrar o menor caminho entre esse vértices e todos os outros

## Links
+ https://www.geeksforgeeks.org/bellman-ford-algorithm-dp-23/
+ https://pt.wikipedia.org/wiki/Algoritmo_de_Bellman-Ford
+ http://scanftree.com/Data_Structure/bellman-ford-algorithm


**Difenrecial**: 
+ Ele é como o djisktra, com o diferencial de que **funciona com arestas negativas**.
+ Mais simples que o djisktra e nâo é guloso como ele.
+ **Distribuido**: Trabalha bem com sistemas dsitribuidos: Exemplo: RIP (vetor de distancia) : algoritmo de roteamento da camda de rede (encontra o caminho de menor custo entre dois roteadores na rede);;;  Bellman-Ford works better (better than Dijksra’s) for distributed systems. Unlike Dijksra’s where we need to find minimum value of all vertices, in Bellman-Ford, edges are considered one by one.
+ O Algoritmo de Dijkstra resolve o mesmo problema, num tempo menor, porém exige que todas as arestas tenham pesos positivos. Portanto, o algoritmo de Bellman-Ford é normalmente usado apenas quando existem arestas de peso negativo.
+ O algoritmo de Bellman-Ford executa em tempo {\displaystyle O(V\times E)}{\displaystyle O(V\times E)} onde V é o número de vértices e E o número de arestas.

**OBS**: A existência e cálculo do caminho mais curto são garantidos caso não
haja a presença de ciclos negativos durante o caminho da origem até
um nó v do grafo. Se há um ciclo negativo, em princípio, o problema não
tem solução, pois o “caminho” pode passar ao longo do ciclo infinitas
vezes obtendo caminhos cada vez menores.

### Complexidade

Desvantagens:
● Tempo maior de execução em comparação com o algoritmo de
Dijkstra
● Alto custo em relação aos casos onde o algoritmo guloso retorna
uma solução ótima

## Como funciona
1. Ecolhe-se um único vértice. Cria um veotr com a distancia para todos os vértices. Todos sâo inciializados com infinito e para ele mesmo, é inicializado como 0 (distancia para ele mesmo = 0 )
2. 


1
A inicialização é uma etapa simples, onde se padroniza os
valores de distância mínima para cada nó. Iremos percorrer todos os
vértices e iremos definir que a sua distância mínima no momento é
infinito, enquanto na origem iremos colocar 0.


2.
● A técnica do relaxamento consiste em verificar se pode ser
encontrado um caminho mais curto para v (do que aquele
encontrado até o momento) passando pelo vértice u. Ou seja,
verificamos se caminho passando pelo vértice u é menor do que
a distância anteriormente calculada.
● Se distância(origem,u) + peso(u,v) \< distancia(origem,v) então:
○ Distância(origem, v) (origem, u) + peso(u,v)
○ Nó predecessor u

3.
Depois de executado (V-1) a técnica do relaxamento, precisamos
verificar se o grafo não contém um ciclo negativo.
● Para verificar se o grafo não contém um ciclo negativo executaremos a
técnica do relaxamento mais uma vez e se conseguirmos minimizar a
distância mínima para qualquer nó provaremos que existe um ciclo
negativo

````
BellmanFord (vértices, arestas, origem)
para cada vértice v em vértices faça: // Inicialização
se v é origem então:
v.distância = 0
senão:
v.distância = infinito
v.anterior = nulo
para i = 1 até tamanho(vértices) - 1: // Relaxamento
para cada aresta uv em arestas faça:
u = uv.origem
v = uv.destino
se v.distância > u.distância + uv.peso então:
v.distância = u.distância + uv.peso
v.anterior = u
para cada aresta uv em arestas faça: // Checagem de ciclos negativos
u = uv.origem
v = uv.destino
se v.distância < u.distância + uv.peso então:
erro "Ciclo de peso negativo"
````

