oponenteN = int(input())
oponenteJog = list(map(int, input().split()))

margeN = int(input())
margeJog = list(map(int, input().split()))
margeJog.sort()

soma = 0
flag = 0
flag2 = 0


for i in range(0, oponenteN):
    for j in margeJog:
        if (j >= oponenteJog[i]):
            soma += j
            margeJog.remove(j)
            break
    flag = 1


if (flag == 1):
    print('impossivel')
else:
    print(soma)