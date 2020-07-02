inteiro = int(input())
flag = 0

for i in range(2, inteiro):
    if(inteiro % i == 0):
        print('nao primo')
        flag = 1
        break

if (flag == 0):
    print('primo')
        