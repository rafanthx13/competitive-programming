class BinaryTree:

    def __init__(self, v = -1):
        self.l = None
        self.r = None
        self.v = v

    def add(self, value):
        if(self.v == -1):
            self.v = value
        self.insert(value)

    def insert(self, value):
        if(self.v == None):
            self.v = value
            return
        if(value > self.v):
            if(self.r == None):
                self.r = BinaryTree(value)
            else:
                self.r.insert(value)
        elif(value < self.v):
            if(self.l == None):
                self.l = BinaryTree(value)
            else:
                self.l.insert(value)

    # Given a non-empty binary search tree, return the node
    # with minum key value found in that tree. Note that the
    # entire tree does not need to be searched
    def __minValueNode(self, node):
        current = node
        while(current.l is not None):
            current = current.l
        return current

    def __maxValueNode(self, node):
        current = node
        while(current.r is not None):
            current = current.r
        return current

    # Usado apra remove_one_node
    def max_node(self, node):
        if(self.leaf(node)):
            return node
        if(node.r is None):
            return self.max_node(node.l)
        return self.max_node(node.r)

    def delete(self, root, value):
        # Base Case
        if(root is None):
            return root

        if(value < root.v):
            root.l = self.delete(root.l, value)
        elif(value > root.v):
            root.r = self.delete(root.r, value)

        else:
            # find value to be removed
            if(root.l is None):
                temp = root.r
                root = None
                return temp

            elif(root.r is None):
                temp = root.l
                root = None
                return temp

            # Há varias formas de refazer a configuração

            # temp = self.__minValueNode(root.r)
            # root.v = temp.v
            # root.r = self.delete(root.r, temp.v)

            temp = self.__maxValueNode(root.l)
            root.v = temp.v
            root.l = self.delete(root.l, temp.v)

            # temp = self.__maxValueNode(root.r)
            # root.v = temp.v
            # root.r = self.delete(root.r, temp.v)

            # temp = self.__minValueNode(root.l)
            # root.v = temp.v
            # root.l = self.delete(root.l, temp.v)

            # 7 4 10 PRE
            # 4 7 10 INF
            # 4 10 7 POS

        return root

    def leaf(self, node):
        return node.r == None and node.l == None

    # Primeiro coisa é já o valor quando esta nele
    # Vai para esquerda e depois para a direita
    # Prefix
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

    def search(self, value):
        if(value == self.v):
            return True
        if(value > self.v):
            if(self.r is None):
                return False
            else:
                return self.r.search(value)
        elif(value < self.v):
            if(self.l is None):
                return False
            else:
                return self.l.search(value)

#####################################

def print_formated(alist):
    last = alist[-1]
    for el in alist:
        if(el != last):
            print(el, end = " ")
        else:
            print(el)

####################################

g = BinaryTree()

# g.add(8)
# g.add(10)
# g.add(4)
# g.add(7)
#
#
# g = g.delete(g, 8)
#
# print_formated(g.pre_ordem([]))
# print_formated(g.em_ordem([]))
# print_formated(g.pos_ordem([]))

# # TEM QU E SER: 4 10 7
# print(g.v)
# print(g.l.v)
# print(g.r.v)

# 7 4 10 PRE
# 4 7 10 INF
# 4 10 7 POS


while(True):
    try:
        inpt = input().split()
        if(len(inpt) == 1):
            inpt = inpt[0]
            if(inpt == "INFIXA"):
                print_formated(g.em_ordem([]))
            elif(inpt == "PREFIXA"):
                print_formated(g.pre_ordem([]))
            elif(inpt == "POSFIXA"):
                print_formated(g.pos_ordem([]))
        else:
            q, v = inpt[0], int(inpt[1])
            if(q == "P"):
                if(g.search(v)):
                    print(v, "existe")
                else:
                    print(v, "nao existe")
            elif(q == "R"):
                g = g.delete(g, v)
            elif(q == "I"):
                g.add(v)
    except EOFError:
        break

# """ REMOVER 8: DEVIA SUBIR 4 EM VEZ DE 4
#     8           10(ERRADO)       4(CERTO)       7
#   /   \        /                   \          4   10
#  4    10      4                    10
#       /        \                   /
#      7          7                 7
# """
