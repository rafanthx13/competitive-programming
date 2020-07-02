def fat(n):
    if n == 0:
        return 1
    else:
        return n * fat(n-1)
    

N = int(input())
OUT = []

for i in range(0, N):
    [A, B, C] = list(map(int, input().split()))

    total = fat(A) / (fat(B) * fat(A - B))

    if total == C:
        OUT.append('Harry esta correto!')
    elif total > C:
        OUT.append('Existem mais combinacoes possiveis!')
    else:
        OUT.append('Existem menos combinacoes possiveis!')

for i in OUT:
    print(i)