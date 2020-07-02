N = int(input())

def fat(n):
    if n == 0:
        return 1
    else:
        return n * fat(n-1)

for i in range(0, N):
    promo = int(input())
    total = fat(10) / fat(20 - promo)
    print(total)
