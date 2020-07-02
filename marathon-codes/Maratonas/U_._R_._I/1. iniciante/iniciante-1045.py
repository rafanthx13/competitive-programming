x = int(input())
y = int(input())

if(x < y):
    h1 = x
    h2 = y
else:
    h1 = y
    h2 = x

soma = 0

flag = True
while(h1 < h2):
    if(h1 % 2 == 0):
        h1 = h1 + 1
        flag = False
    if(flag):
        h1 = h1 + 2
        flag = False
    soma = soma + h1
    h1 = h1 + 2

print(soma)
