# Accepted

qtd_alunos, min_pessoas = list(map(int, input().split()))
horario_alunos = list(map(int, input().split()))

c = 0
for h in horario_alunos:
    if(h <= 0):
        c +=1

if(c >= min_pessoas):
    print("YES")
else:
    print("NO")

# c = 0
# for h in horario_alunos:
#     if(h >= 0):
#         c +=1
#
# if(c >= min_pessoas):
#     print("YES")
# else:
#     print("NO")
