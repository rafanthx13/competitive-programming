def dist (p):
    count = 0 
    aux = []
    for i in p:
        if p.count(i) > 1 and i not in aux:
            count += 1
            aux.append(i)

    return count

def fat(n):
    if n == 0:
        return 1
    else:
        return n * fat(n-1)

N = int(input())

for i in range(0, N):
    x = list(map(int, input().split()))
    y = (6 - dist(x))
    total = y * (y-1) * (y-2) *( y-3)
    print(total)