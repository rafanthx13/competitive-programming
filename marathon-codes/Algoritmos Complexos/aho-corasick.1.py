class AhoNode:

    # Função Construtora
    def __init__(self):
        self.isWord = False
        self.gotoRight = {}
        self.out = []
        self.fail = None

    # TESTE: ['an', 'ant', 'cant', 'deca', 'decant', 'plant']
    #        [ 1  ,   2  ,   3,  ,   -   ,     4   ,    -   ]

    # Criar inicio do grafo
    def aho_start(list_words):
        root = AhoNode()
        for word in list_words:
            for letter in word:
                root.gotoRight.setdefault(letter, AhoNode())
        return root

    # Criar automato
    def aho_automato(list_words):
        root = aho_start(list_words)
        queue = [] # append poe no fim (empilha) | pop() tira do fim (desempilha)

