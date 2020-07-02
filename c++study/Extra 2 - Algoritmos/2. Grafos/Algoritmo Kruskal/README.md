# Algoritmo Kruskal

Problema:  Encontrar uma MST (árvore geradora de custo mínimo) de um grafo não-dirigido com custos nas arestas.

Links:
+ https://pt.wikipedia.org/wiki/Algoritmo_de_Kruskal
+ https://www.ime.usp.br/~pf/algoritmos_para_grafos/aulas/kruskal.html
+ https://www.ime.usp.br/~maratona/aulas/union-find-e-kruskal

Dado um grafo ponderado (as arestas tem pesos), encontre uma árvore geradora mínima, ou seja, encontre uma árvore que tenha todos os nós do grafo cujo a soma dos pesos seja a menor possível.

Este é um algorimo guloso (a estratégia é colher a melhor opção no momneto, na esperança de que esta escolha leve a solução ótima global).

Idea do Algoritmo
1. Escolho as arestas de menor tamanho (algoritmo guloso)
2. Marque-a como um grafo e verifique se tem ciclo
3. Se houver ciclo, não adiciona esa aresta

## Union Find

Algoritmo para detectar ciclos em grafos sem direção. Será um algoritmo auxiliar para resolver nosso problema