# U_R_I - 1195 - 7. Grafos - Agosto de 2019 - Assunto: Árvore binária

# DEu time_limit: link para c++ enviado ()

# Em computação, a árvores binária de busca ou árvore binária de pesquisa é uma estrutura 
# baseada em nós (nodos), onde todos os nós da subárvore esquerda possuem um valor numérico inferior 
# ao nó raiz e todos os nós da subárvore direita possuem um valor superior ao nó raiz 
# (e assim sucessivamente). O objetivo desta árvore é estruturar os dados de forma flexível, 
# permitindo a busca binária de um elemento qualquer da árvore.

# A grande vantagem das árvores de busca binária sobre estruturas de dados convencionais é que os
#  algoritmos de ordenação (percurso infixo) e pesquisa que as utilizam são muito eficientes.

# Para este problema, você receberá vários conjuntos de números e a partir de cada um dos conjuntos, 
# deverá construir uma árvore binária de busca. Por exemplo, a sequência de valores:
#  8 3 10 14 6 4 13 7 1 resulta na seguinte árvore binária de busca:

# Entrada
# A entrada contém vários casos de teste. A primeira linha da entrada contém um inteiro C (C ≤ 1000),
#  indicando o número de casos de teste que virão a seguir. Cada caso de teste é composto por 2 linhas.
#  A primeira linha contém um inteiro N (1 ≤ N ≤ 500) que indica a quantidade de números que deve
#  compor cada árvore e a segunda linha contém N inteiros distintos e não negativos, separados por um espaço em branco.

# Saída
# Cada linha de entrada produz 3 linhas de saída. Após construir a árvore binária de busca com os 
# elementos de entrada, você deverá imprimir a mensagem "Case n:", onde n indica o número do caso
#  de teste e fazer os três percursos da árvore: prefixo, infixo e posfixo, apresentando cada um 
# deles em uma linha com uma mensagem correspondente conforme o exemplo abaixo, separando cada 
# um dos elementos por um espaço em branco. 

# Obs: Não deve haver espaço em branco após o último item de cada linha e há uma linha em branco 
# após cada caso de teste, inclusive após o último.


# Exemplo de Entrada	Exemplo de Saída

# 2

# 3
# 5 2 7

# 9
# 8 3 10 14 6 4 13 7 1

# Case 1:
# Pre.: 5 2 7
# In..: 2 5 7
# Post: 2 7 5

# Case 2:
# Pre.: 8 3 1 6 4 7 10 14 13
# In..: 1 3 4 6 7 8 10 13 14
# Post: 1 4 7 6 3 13 14 10 8

#         8
#       3   10
#     1  6     14
#       4 7   13

# Solução:
## Pre-Ordem: Busca em profundidade imprimindo cada no que encontrar (Left -> Right)
## Em-Ordem : Busca em profundidade e imprime sempre o da esquerda primeiro (Left -> Right)
## Pos-Ordem: Busca em profundidade e so imprime se nao tiver mais nada a ser buscado (Left -> Right)
### Consequentemente teremos tambem
## Invertida-Ordem: Busca em Profundidade que imprime o da direita primeiro (Right -> Left)

class Node:

    # Primeiro coisa é já o valor quando esta nele
    # Vai para esquerda e depois para a direita
    def pre_ordem(self, lista):
        lista.append(self.v) # No inicio
        if(self.l):
            self.l.pre_ordem(lista)
        if(self.r):
            self.r.pre_ordem(lista)
        return lista

    # So adiciona depois de percorrer todos os da esquerda
    def em_ordem(self, lista):
        if(self.l):
            self.l.em_ordem(lista)
        lista.append(self.v) # No Meio
        if(self.r):
            self.r.em_ordem(lista)
        return lista

    def pos_ordem(self, lista):
        if(self.l):
            self.l.pos_ordem(lista)
        if(self.r):
            self.r.pos_ordem(lista)
        lista.append(self.v) # No fim
        return lista

    def __init__(self, valor):
        self.l = None   # Left Node
        self.r = None   # Right Node
        self.v = valor  # Value

    def insert(self, valor):
        # inserir a direita
        if(valor > self.v):
            if(self.r == None):
                self.r = Node(valor)
            else:
                self.r.insert(valor)
        # inserir a esquerda
        if(valor < self.v):
            if(self.l == None):
                self.l = Node(valor)
            else:
                self.l.insert(valor)

def print_list(lista):
    for i in lista[:-2]:
        print(i, end = " ")
    print(lista[-1])
    

n = int(input())

for i in range(n):

    number = input()
    inputs = list(map(int, input().split()))

    root_grafo = Node(inputs.pop(0))
    for v in inputs:
        root_grafo.insert(v)

    pre = root_grafo.pre_ordem([])
    em  = root_grafo.em_ordem([])
    pos = root_grafo.pos_ordem([])

    print("Case", str(i+1) + ":")
    print("Pre.:", end=" ")
    print_list(pre)
    print("In..:" , end=" ")
    print_list(em)
    print("Post:" , end=" ")
    print_list(pos)

    if(i != n-1):
        print()
