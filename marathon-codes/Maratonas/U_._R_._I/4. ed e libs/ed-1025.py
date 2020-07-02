# U_R_I - 1025 - 6. Ed e Libs - Sort - Agosto de 2019

#  Raju e Meena adoram jogar um jogo diferente com pequenas peças
#  de mármores, chamados Marbles. Eles têm um monte destas peças 
#  com números escritos neles. No início, Raju colocaria estes pequenos
#  mármores um após outro em ordem ascendente de números escritos neles.
#  Então Meena gostaria de pedir a Raju para encontrar o primeiro mármore
#  com um certo número. Ele deveria contar 1...2...3. Raju ganha um ponto
#  por cada resposta correta e Meena ganha um ponto se Raju falha. Depois 
#  de um número fixo de tentativas, o jogo termina e o jogador com o máximo
#  de pontos vence. Hoje é sua chance de jogar com Raju. Sendo um/a cara 
#  esperto/a, você tem em seu favor o computador. Mas não subestime Meena,
#  ela escreveu um programa para monitorar quanto tempo você levará para 
#  dar todas as respostas. Portanto, agora escreva o programa, que ajudará
#  você em seu desafio com Raju.


# Entrada
# A entrada contém vários casos de teste, mas o total de casos é menor 
# do que 65. Cada caso de teste inicia com dois inteiros: N que é o número
#  de mármores e Q que é o número de consultas que Meena deseja fazer. 
# As próximas N linhas conterão os números escritos em cada um dos N mármores.
#  Os números destes mármores não tem qualquer ordem em particular. As seguintes
#  Q linhas irão conter Q consultas. Tenha certeza, nenhum dos números da entrada
#  é maior do que 10000 e nenhum deles é negativo.
# A entrada é terminada por um caso de teste onde N = 0 e Q = 0.

# Saída
# Para cada caso de teste de saída deve haver um número serial do caso de teste. 
# Para cada consulta, escreva uma linha de saída. O formato desta linha dependerá 
# se o número consultado estiver ou não escrito em um dos mármores. Os dois diferentes formatos são descritos abaixo:
# 'x found at y', se o primeiro marble x foi encontrado na posição y. Posições são numeradas de 1, 2,...  a N.
# 'x not found', se o marble com o número x não estiver presente.
# Exemplo de Entrada	Exemplo de Saída

# 4 1           # 5 2

# 2             # 1
# 3             # 3
# 5             # 3 
# 1             # 3
                # 1

# 5             # 2
                # 3

# CASE# 1:      # CASE# 2:
# 5 found at 4  # 2 not found
                # 3 found at 3


# Solução: Ordenar AS entrada e verificar o index (contando a partir de 1) se está ou não.
## Problemas encontrado: Tem que ser extremamente eficeinte. Por isos, usei quick sort e busca binaria
##  OBS: Na busca binaria, você tem que achar a primeira ocorrencia. Da forma manual nâo deu muito certo
##    Uma solução que deu certo foi usar "from bisect import bisect_left" que me pareceu eficiente

#########################

from bisect import bisect_left 
  
def BinarySearch(a, x): 
    i = bisect_left(a, x) 
    if i != len(a) and a[i] == x: 
        return i 
    else: 
        return -1

def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than or 
        # equal to pivot 
        if   arr[j] <= pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  
# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
  
# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 

#########################

c = 0

while(True):
  
  c += 1
  qtd, querys = list(map(int, input().split()))
  if(qtd == 0 and querys == 0):
    break

  aList = []
  for _ in range(qtd):
    aList.append(int(input()))

  aListQuerys = []
  for _ in range(querys):
    aListQuerys.append(int(input()))

  quickSort(aList,0, qtd - 1)

  print("CASE# " + str(c) + ":")

  for query in aListQuerys:
    try:
      found_index = BinarySearch(aList, query) + 1
      if(found_index != 0):
        print(query, "found at", found_index)
      else:
        print(query, "not found")
    except Exception:
      print(query, "not found")
