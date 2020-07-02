#########  Strings de Inicialização
string_pessoas = """
Capheus 1
Nomi 8
Lito 1
Will 1
Kala 1
Wolfgang 1
Sun 1
Riley 1
Abner 5
""".split("\n")[1:-1]

string_links = """
Capheus Nomi
Nomi Lito
Lito Will
Will Kala
Kala Wolfgang
Wolfgang Sun
Sun Riley
""".split("\n")[1:-1]

string_querys = """
Lito
Nomi
Abner
""".split("\n")[1:-1]


######### START INPUTS

n_pessoas, qtd_ligacoes, querys = [9 , 7, 3]
# n_pessoas, qtd_ligacoes, querys = list(map(int, input().split()))

pessoas = []
candidatos = []
links = []
rank_dict = {}
parent_dict = {}

# for _ in range(n_pessoas):
#     nome, level = input().split()
#     pessoas.append((nome, int(level)))
#     rank_dict[nome] = level

for p in string_pessoas:
    nome, level = p.split()
    rank_dict[nome] = int(level)

# for _ in range(qtd_ligacoes):
#     p1, p2 = input().split()
#     links.append([p1,p2])

# for l in string_links:
#     l1, l2 = l.split()
#     parent_dict[l1] = l2

# for _ in range(querys):
#     candidatos.append(input())

for q in string_querys:
    candidatos.append(q)

######### PROCESSING



# load links
# for v1, v2 in links:
#     parent_dict[v1] = v2

######### Union-Find defs

def find(parent_dict, p):
    if(parent_dict[p] == -1):
        return p
    else:
        parent_dict[p] = find(parent_dict, parent_dict[p])
    return parent_dict[p]

def union(parent_dict, rank_dict, p1, p2):
    if(rank_dict[p1] > rank_dict[p2]):
        parent_dict[p2] = p1
    elif(rank_dict[p1] < rank_dict[p2]):
        parent_dict[p1] = p2
    else:
        rank_dict[p1] = p2

def query_valid_player(parent_dict, rank_dict, set_sensate, p):
    # 1. Cond : nao ser sensate
    if( p not in set_sensate):
        return True
    # 3. Cond : ser ssensate com lv maior que 5
    if(rank_dict[p] > 5):
        return True
    # 2. Cond : Ser sensate e ninguem no grupo ter level >5
    if(rank_dict[find(parent_dict, p)] <= 5):
        return True
    else:
        return False

### varredura para Unir tudo para ficar otimizado

# load pessoas
for a in string_pessoas:
    n, l = a.split()
    parent_dict[n] = -1

set_sensate = set()

for l in string_links:
    p1, p2 = l.split()
    set_sensate.add(p1)
    set_sensate.add(p2)
    print("p1", p1, "p2", p2)
    x = find(parent_dict, p1)
    y = find(parent_dict, p2)
    union(parent_dict, rank_dict, x , y)

print("parent_dict", parent_dict)
print("rank_dict", rank_dict)

print()

for q in string_querys:
    if(query_valid_player(parent_dict, rank_dict, set_sensate, q)):
        print("S")
    else:
        print("N")
