N = int(input())
OUT = []

for i in range(0, N):
    x = int(input())
    total = pow(2, x)
    OUT.append(str(int(total)) + ' numeros.')


for i in OUT:
    print(i)