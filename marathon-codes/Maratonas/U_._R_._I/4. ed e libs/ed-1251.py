# U.R.I. - 1161 - 5. Matematica - Matematica, Fatorial - Agosto de 2019 (All Right)

# Dada uma linha de texto, você deve encontrar as frequências de cada um 
# dos caracteres presentes nela. As linhas fornecidas não conterão nenhum
#  dos primeiros 32 ou dos últimos 128 caracteres da tabela ASCII. É claro
#  que não estamos levando em conta o caracter de fim de linha.

# Entrada
# A entrada contém vários casos de teste. Cada caso de teste é composto por
#  uma única linha de texto com até 1000 caracteres.

# Saída
# Imprima o valor ASCII de todos os caracteres presentes e a sua frequência 
# de acordo com o formato abaixo. Uma linha em branco deverá separar 2 conjuntos
#  de saída. Imprima os caracteres ASCII em ordem ascendente de frequência. 
# Se dois caracteres estiverem presentes com a mesma quantidade de frequência,
#  imprima primeiro o caracter que tem valor ASCII maior. A entrada é terminada por final de arquivo (EOF).

# Exemplo 
#  Entrada	      Saída

# AAABBC        # 122333
# 67 1          # 49 1
# 66 2          # 50 2
# 65 3          # 51 3



##  A saida tem que duplamente ordenada, em forma ascendente de valor e depois em forma descendente de valor ASCI
## OBS2: Deve haver um new_line apos entre os casos, mas isso é na saida. Assim, useis a flag para pular depois da entrada de dados
##        Se você rodar em seu console fica estranho, mas A SAIDA E ENTRDA SAO COISAS DIFERENTES QUANDO O U.R.I EXECUTA

# Como foi resolvido: 
# 1. Usamos um DIct para contar (character_ascci, freq)
#         h = { char_ascci, freq}
# 2. Depois agrupamos todos os character_ascci num outro dicionary cuja chave é a frequencia
#         hh = { freq, [char_ascci]}
# 3. Ordena internamente cada lista de char_ascci
# 4. Para imprimir, criamos uma lsita de chaves ordenads (ascendetes) e pegamos cada lista e vamos percorrela revetida (descendente)[::-1]


def partition(arr,low,high): 
    i = ( low-1 )          
    pivot = arr[high]     
    for j in range(low , high): 
        if   arr[j] <= pivot: 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  
def quickSort(arr,low,high): 
    if low < high: 
        pi = partition(arr,low,high) 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 

flag = 0
while(True):
  try:

    h = {}
    hh = {}
    s = input()

    if(flag == 1):
      print()

    for w in s:
      w = ord(w)
      if(w not in h):
        h[w] = 1
      else:
        h[w] += 1

    # Ordenacao de forma ascendente por quantidade (mapeando para hash)
    for key,value in h.items():
      if(value not in hh):
        hh[value] = []
        hh[value].append( key )
      else:
        hh[value].append( key )
    
    # Ordenando internamente
    for alist in hh:
      quickSort(hh[alist], 0, len(hh[alist]) - 1)

    sorted_qtd = sorted(hh.keys())

    for ord_key in sorted_qtd:
      aList = hh[ord_key]
      for ascci_number in aList[::-1]:
        print(ascci_number, ord_key)

    flag = 1
    
  except EOFError:
    break

