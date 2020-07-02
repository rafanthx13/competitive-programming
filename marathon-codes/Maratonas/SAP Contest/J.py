# Accepted

n = int(input())
horario_alunos = list(map(int, input().split()))

c = 0
for i in horario_alunos:
    if(i == 1):
        c += 1

print(c)
