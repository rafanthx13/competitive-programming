# U_R_I - 6. Paradigmas - Agosto de 2019 - Greedy 

# Todos os anos, artistas de todo o mundo se reúnem na cidade, 
# onde fazem esculturas de gelo gigantescas. A cidade vira uma 
# galeria de arte ao céu aberto, uma vez que as esculturas ficam 
# expostas na rua por semanas, sem derreter. Afinal, a temperatura
#  média no inverno de Harbin (época em que ocorrerá a final mundial do ICPC) é de -20 graus.

# O primeiro passo para fazer a escultura é montar um grande bloco
#  de gelo da dimensão pedida pelo artista. Os blocos são recortados
#  das geleiras de Harbin em blocos de altura e profundidade padrão e
#  vários comprimentos diferentes. O artista pode determinar qual o 
# comprimento que ele deseja que tenha o seu bloco de gelo para que a escultura possa começar a ser esculpida.

# Os comprimentos disponíveis dos blocos são {a1; a2; ...;  aN} e o 
# comprimento que o artista deseja é M. O bloco de comprimento 1 é 
# muito usado, por este motivo ele sempre aparece na lista de blocos disponíveis.
#  Sua tarefa é determinar o número mínimo de blocos tal que a soma de seus comprimentos seja M.

# Entrada
# A entrada é composta por diversas instâncias. A primeira linha da entrada contém um inteiro T
#  indicando o número de instâncias. A primeira linha de cada instância contém 
# dois inteiros N (1 ≤ N ≤ 25) e M (1 ≤ M ≤ 1000000) representando o número de tipos de blocos
#  e o comprimento desejado pelo artista, respectivamente. A próxima linha contém os inteiros 
# a1; a2; ...; aN , onde (1 ≤ ai ≤ 100) para todo i (1,2,...N) separados por espaço.

# Saída
# Para cada instância, imprima o número mínimo de blocos necessários para obter um bloco de comprimento M.

# Exemplo de Entrada	Exemplo de Saída

# 2

# 6 100
# 1 5 10 15 25 50     # 2

# 2 103 
# 1 5                 # 23

# Solução: NÃO É GREEDY, é como o problema das hastes, a melhor escolha no momento não é garantia
# ENtão a soluçâo é fazer todas as possibilidades


# n = int(input())

# for _ in range(n):

#   qtd, total = list(map(int, input().split()))

#   listPieces = list(map(int, input().split()))

#   listPieces.sort()

#   count = 0

#   for p in listPieces[::-1]:
#     # print("p")
#     aux = total
#     qtd_p = total // p
#     rest = total % p
#     count += qtd_p
#     print("\t p:", p, "||total antes:", aux, "|| qtd_p", qtd_p, "|| count", count, "|| rest", rest)
#     if(rest == 0):
#       break
#     total = rest
  
#   print(count)

# from sys import maxint

max_number = 1000001 # poderia ser de algum import

# Programação Dinâmica
def minimum_blocks(listaPieces, qtd, total):
    
    # inicializar vetor para salvar (ocupa muita memoria)
    dp = {0: 0}
    for j in range(1, total + 1):
        dp[j] = max_number
    rest = 1

    # print(dp)

    while(rest <= total):
      for k in range(qtd):
        if(listaPieces[k] <= rest): # da pra diminuir
          temp = dp[rest - listaPieces[k]]
          if temp != max_number and temp + 1 < dp[rest]:
            dp[rest] = 1 + temp
      rest += 1
    return dp[total]

t = int(input())

for i in range(t):

    qtd, total = list(map(int, input().split()))
    listaPieces = list(map(int, input().split()))

    print(minimum_blocks(listaPieces, qtd, total))




# 5 17718
# 1 2 8 9 13          # 1364
# 11 22789
# 1 9 10 16 24 25 29 37 40 42 49  # 466
# 11 7572
# 1 3 12 15 17 18 24 33 40 48 52 # 146
# 12 10970
# 1 2 6 11 12 15 18 22 29 37 38 46 # 239



