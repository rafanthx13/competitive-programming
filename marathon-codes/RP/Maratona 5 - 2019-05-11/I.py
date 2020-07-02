
def fat(n):
    if n == 0:
        return 1
    else:
        return n * fat(n-1)

def anagrama(p):
    repeat = 1
    aux = []

    for c in p:
        count = p.count(c)
        if count > 1 and c not in aux:
            aux.append(c)
            repeat *= fat(count)

    return int(fat(len(p)) / repeat)

N = int(input())
OUT = []

for i in range(0, N):
    P1 = input()
    P2 = input()

    a1 = anagrama(P1)
    a2 = anagrama(P2)

    if a1 == a2:
        OUT.append('As strings tem a mesma quantidade de anagramas:')
        OUT.append(a1)
    elif a1 > a2:
        OUT.append(P1 + ' tem mais anagramas:')
        OUT.append(a1)
    else:
        OUT.append(P2 + ' tem mais anagramas:')
        OUT.append(a2)


for i in OUT:
    print(i)

