# 1555 - Funções
times = int(input())

final_list = []
for i in range(times):
    list_of_inputs = input().split()
    x = int(list_of_inputs[0])
    y = int(list_of_inputs[1])

    rafa = ((3*x) ** 2) + (y ** 2)
    beto = 2*(x ** 2) + ((5 * y) ** 2)
    carlos = (-100 * x) + (y ** 3)

    winer = None

    if( rafa > beto and rafa > carlos):
        winer = 'Rafael'
    elif (beto > rafa and beto > carlos):
        winer = 'Beto'
    else:
        winer = 'Carlos'

    final_list.append(winer)

for x in final_list:
    print(x, 'ganhou')
