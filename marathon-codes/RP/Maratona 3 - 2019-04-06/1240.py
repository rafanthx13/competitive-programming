# 1240 - Encaixa ou Não I

times = int(input())

final_list = []

for i in range(times):
    flag = False
    list_of_inputs = input().split()
    x = str(list_of_inputs[0])
    y = str(list_of_inputs[1])

    size = len(x)
    for i in range(size):
        if( x[i:] == y ):
            final_list.append('encaixa')
            flag = True
    if(flag):
        continue
    final_list.append('nao encaixa')

for x in final_list:
    print(x) 
