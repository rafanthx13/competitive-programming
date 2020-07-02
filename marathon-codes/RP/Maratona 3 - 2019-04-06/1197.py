# 1197 - Volta à Faculdade de Física
while True:
    try:
        inputs = []
        list_of_inputs = input().split()
        v = list_of_inputs[0]
        t = list_of_inputs[1]
        print(int(v) * (int(t)*2) )
    except EOFError:
        break
