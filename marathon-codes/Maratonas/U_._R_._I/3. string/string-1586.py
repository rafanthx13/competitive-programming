# João desafiou Pedro em um jogo envolvendo sequências de letras.

#  No início, é mostrado aos jogadores uma sequência de letras.
#  Cada jogador deve tentar usar essa sequência para formar outras sequências.
#  Para isso, é permitido remover algumas letras da sequência, sem alterar a ordem.
#  O jogador que conseguir formar mais sequências ganha o jogo.

# Pedro gostaria de sua ajuda para ganha de João. Sua tarefa é mostrar para Pedro todas as sequências distintas, 
# em ordem alfabética, que ele pode formar durante o jogo.

# Entrada
# A entrada contém vários casos de teste. Cada caso de teste consiste de uma linha contendo uma 
# sequência a ser usada no jogo. A sequência é formada apenas por caracteres minúculos e pode possuir até 1000 caracteres.

# Saída
# Para cada teste, a saída consiste de várias linhas, contendo todas as sequências que podem ser 
# formadas por Pedro durante o jogo. É garantido para todas as entradas que não haverá mais de 1000
#  sequências possíveis de ser formadas. Imprima uma linha em branco após cada caso de teste.

# Exemplo de Entrada	Exemplo de Saída

# abc
# aaaaa
# huehue

# a
# ab
# abc
# ac
# b
# bc
# c

# a
# aa
# aaa
# aaaa
# aaaaa

# e
# ee
# eh
# ehe
# ehu
# ehue
# eu
# eue
# h
# he
# hee
# heh
# hehe
# hehu
# hehue
# heu
# heue
# hh
# hhe
# hhu
# hhue
# hu
# hue
# huee
# hueh
# huehe
# huehu
# huehue
# hueu
# hueue
# huh
# huhe
# huhu
# huhue
# huu
# huue
# u
# ue
# uee
# ueh
# uehe
# uehu
# uehue
# ueu
# ueue
# uh
# uhe
# uhu
# uhue
# uu
# uue

while(True):
  try:
    word = input()
    dic = {}
    output = []
    c = 1
    for w in word:
      dict.setdefault(w, c)
      c += 1
    
    

    
  except EOFError:
    break