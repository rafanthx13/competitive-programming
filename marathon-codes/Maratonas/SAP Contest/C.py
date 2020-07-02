n = int(input())

qtd_ce, qtd_tra = list(map(int, input().split()))

grafo = {i:[] for i in range(1,qtd_ce)}

for _ in qtd_tra:
    v1, v2, t = list(map(int, input().split()))
    grafo[v1].append(v2)
