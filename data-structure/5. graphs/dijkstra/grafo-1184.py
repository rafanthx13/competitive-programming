# br.SPOJ PAISES- https://br.spoj.com/problems/PAISES/

INFINITO = 1999

def minDist(dist, visit, qtd_cidades):
    minimun = INFINITO
    error = -1
    # print("aaa")
    # print("d:", dist)

    for v in range(1, qtd_cidades + 1):
        if(dist[v] < minimun and not visit[v]):
            # print("entrou")
            minimun = dist[v]
            min_index = v
            error = 1
    # print("abb")
    if(error == -1):
        return error
    return min_index

def dijkstra(src, dest, grafo, qtd_cidades):
    # Inicializar
    dist = {i:INFINITO for i in range(1,qtd_cidades + 1)}
    dist[src] = 0
    visit = { j:False for j in range(1, qtd_cidades + 1)}
    # dijisktra
    for _ in range(1, qtd_cidades + 1):
        u = minDist(dist, visit, qtd_cidades)
        if(u == -1):
            # print("error")
            return dist
        visit[u] = True
        # print("u", u)
        for v in grafo[u].keys():
            # print("v", v, "u", u, "Grafo[u][v]", grafo[u][v])
            # print("grafo[u][v]", grafo[u][v])
            # print("visit[V]", visit[v])
            # print("dist[v] > dist[u] + grafo[u][v]", dist[v] > dist[u] + grafo[u][v], dist[v], dist[u], grafo[u][v])

            if(grafo[u][v] >= 0 and
                visit[v] == False and
                dist[v] > dist[u] + grafo[u][v]
            ):
                # print("dist", v, "=", dist[u] + grafo[u][v])
                dist[v] = dist[u] + grafo[u][v]
        print("\n")
    # retornar com o array das distancias
    return dist

def instantaneo(src, dest, grafo):
    return dest in grafo[src].keys() and src in grafo[dest].keys()

def check_instataneo(src, dest, grafo):
    return src in grafo[dest]

while(True):
    cidades, mensagens = list(map(int, input().split()))
    if(cidades == 0 and mensagens == 0):
        break
    # Make Graph
    grafo = { i:{} for i in range(1,cidades+1)}
    dict_dist = {}
    # Processar arestas
    for _ in range(mensagens):
        v1, v2, v = list(map(int, input().split()))
        if(check_instataneo(v1,v2,grafo)):
            grafo[v1][v2] = 0
            grafo[v2][v1] = 0
        else:
            grafo[v1][v2] = v
    # Respondeer
    querys = int(input())
    for _ in range(querys):
        a, b  = list(map(int, input().split()))
        # EH instataneo
        if(instantaneo(a,b,grafo)):
            print(0)
            continue
        # djikstra : evitar fazer varias vezes
        if(a not in dict_dist):
            dict_dist[a] = dijkstra(a,b,grafo,cidades)
        # print(dict_dist)
        if(dict_dist[a][b] == INFINITO):
            print("Nao e possivel entregar a carta")
        else:
            print(dict_dist[a][b])

    # print("==================")
