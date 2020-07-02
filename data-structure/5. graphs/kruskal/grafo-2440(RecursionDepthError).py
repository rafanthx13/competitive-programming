# URI 2440, br.SPOJ TROIA13 - Grafos - Outubro de 2019
# Assunto: Grafos, MST, Kruskal
# RecursionError: maximum recursion depth exceeded in comparison]

def dfs(node, visit):
    if(visit[node]):
        return
    visit[node] = True
    for depth_node in grafo[node]:
        dfs(depth_node, visit)

vertices, arestas = list(map(int, input().split()))

grafo = { i:[] for i in range(0, 50001)}
visit = [False]*(50001)

vertices = [i for i in range(1, vertices + 2)]

for _ in range(arestas):
     v1, v2 = list(map(int, input().split()))
    grafo[v1].append(v2)
    grafo[v2].append(v1)

count = 0
for node in range(1, vertices + 1):
    if(not visit[node]):
        dfs(node, visit)
        count += 1

print(count)
