def fat(n):
    if n == 0:
        return 1
    else:
        return n * fat(n-1)
    

N = int(input())
OUT = []

for i in range(0, N):
    x = int(input())

    total = (fat(x) / (fat(2) * fat(x - 2))) + 4
    OUT.append(int(total))

    
for i in OUT:
    print(i)