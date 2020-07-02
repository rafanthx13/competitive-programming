def fat(n):
    if n == 0:
        return 1
    else:
        return n * fat(n-1)

N = int(input())
OUT = []

for i in range(0, N):
    x = int(input())
    f = fat(x)
    OUT.append(str(f) + ' maneiras diferentes, senhor John!')

for i in OUT:
    print(i)