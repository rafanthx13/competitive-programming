
def func(l, n):
    totalL = 26
    totalN = 10
    
    combinacaoL = totalL * l
    combinacaoN = totalN * n

    return combinacaoL + combinacaoN

default = func(3,4)

OUT = []

while True:
    try:
        [L, N] = list(map(int, input().split()))
        new = func(L, N)
        if new == default:
            print('A nova codificacao eh igual!')
        elif new > default:
            print('A nova codificacao eh melhor!')
        else:
            print('A nova codificacao eh pior!')
    except EOFError:
        break
