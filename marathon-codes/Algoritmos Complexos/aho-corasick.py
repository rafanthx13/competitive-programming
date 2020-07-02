class AhoNode:
    def __init__(self):
        self.goto = {}
        self.out = []
        self.fail = None
 
def aho_create_forest(patterns):
    root = AhoNode()
 
    for path in patterns:
        node = root
        for symbol in path:
            node = node.goto.setdefault(symbol, AhoNode())
        node.out.append(path)
    return root
 
 
def aho_create_statemachine(patterns):
    root = aho_create_forest(patterns)
    queue = []
    for node in root.goto.values():
        queue.append(node)
        node.fail = root
 
    while len(queue) > 0:
        rnode = queue.pop(0)
 
        for key, unode in rnode.goto.items():
            queue.append(unode)
            fnode = rnode.fail
            while fnode != None and not (key in fnode.goto):
                fnode = fnode.fail
            unode.fail = fnode.goto[key] if fnode else root
            unode.out += unode.fail.out
 
    return root
 
 
def aho_find_all(s, root, callback):
    node = root
 
    for i in range(len(s)):
        while node != None and not (s[i] in node.goto):
            node = node.fail
        if node == None:
            node = root
            continue
        node = node.goto[s[i]]
        for pattern in node.out:
            callback(i - len(pattern) + 1, pattern)
 
############################
# Demonstration of work
def on_occurence(pos, patterns):
    print("At pos: " +  str(pos) + " found pattern: " + str(patterns) )
 
# patterns = ['a', 'ab', 'abc', 'bc', 'c', 'cba']
patterns = ['an', 'ant', 'cant', 'deca', 'decant', 'plant']
s = "ant"
print("Input:", s)
root = aho_create_statemachine(patterns)
aho_find_all(s, root, on_occurence)

# TESTE: ['an', 'ant', 'cant', 'deca', 'decant', 'plant']
#        [ 1  ,   2  ,   3,  ,   -   ,     4   ,    -   ]

# https://en.wikipedia.org/wiki/Trie
# https://www.geeksforgeeks.org/aho-corasick-algorithm-pattern-searching/

# Para aplicar:
##### O aho-corasick deve ser aplicado sobre o proprio dicionário

# Input: decant
# At pos: 0 found pattern: deca
# At pos: 3 found pattern: an
# At pos: 0 found pattern: decant
# At pos: 2 found pattern: cant
# At pos: 3 found pattern: ant

# Se você ordenar pelo patters, se cada elemento perte