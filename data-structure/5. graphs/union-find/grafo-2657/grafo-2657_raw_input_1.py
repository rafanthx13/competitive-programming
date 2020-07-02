#########  Strings de Inicialização
string_pessoas = """
A 6
B 10
C 6
D 2
E 1
F 4
G 0
H 6
I 3
J 1
K 8
L 7
M 5
N 3
O 7
P 4
Q 9
R 10
S 2
T 0
U 10
V 8
W 5
X 0
Y 4
Z 6
""".split("\n")[1:-1]

string_links = """
C A
D A
D B
D C
E B
E C
F A
F C
F D
F E
G A
G B
G C
G D
G E
H A
H B
H C
H D
H E
H G
I A
I B
I C
I E
I G
I H
J D
J E
J F
J I
K B
K C
K D
K H
K I
L B
L C
L E
L G
L I
L J
L K
M A
M B
M C
M E
M F
M I
M J
M L
N A
N C
N D
N E
N F
N H
N L
N M
O A
O B
O E
O F
O H
O I
O J
O L
O N
P A
P B
P D
P I
P J
P K
P M
Q A
Q B
Q C
Q D
Q F
Q H
Q I
Q J
Q L
Q M
Q O
Q P
R B
R C
R D
R F
R G
R I
R K
R L
R M
R O
S A
S B
S F
S G
S H
S J
S N
S P
S R
T B
T D
T E
T G
T H
T I
T O
T P
T Q
T R
T S
U B
U D
U E
U F
U G
U J
U K
U L
U M
U O
U P
U R
U S
U T
V A
V B
V C
V F
V I
V J
V K
V L
V M
V Q
V S
V U
W C
W D
W E
W F
W K
W M
W N
W O
W P
W R
W S
W U
W V
X B
X C
X D
X E
X G
X H
X I
X J
X L
X P
X Q
X R
X S
X U
X W
Y A
Y B
Y D
Y E
Y G
Y J
Y K
Y M
Y N
Y O
Y P
Y R
Y U
Y V
Y X
Z B
Z D
Z E
Z H
Z I
Z J
Z N
Z P
Z Q
Z R
Z T
Z U
Z W
Z X
""".split("\n")[1:-1]

string_querys = """
A
B
C
D
E
F
G
H
I
J
K
L
M
N
O
P
Q
R
S
T
U
V
W
X
Y
Z
""".split("\n")[1:-1]


######### START INPUTS

n_pessoas, qtd_ligacoes, querys = [26, 200, 26]
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
        parent_dict[p1] = p2

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

print("parent_dict", parent_dict)
print("rank_dict", rank_dict)

for l in string_links:
    p1, p2 = l.split()
    set_sensate.add(p1)
    set_sensate.add(p2)
    print("p1", p1, "p2", p2)
    x = find(parent_dict, p1)
    y = find(parent_dict, p2)
    if(x != y):
        union(parent_dict, rank_dict, x , y)



print()

for q in string_querys:
    if(query_valid_player(parent_dict, rank_dict, set_sensate, q)):
        print("S")
    else:
        print("N")
