# Gene e Gina possuem um tipo peculiar de fazenda. Ao invés de criar animais
#  e plantar vegetais como acontece em fazendas normais, eles cultivam strings.
#  Uma string é uma sequência de caracteres. As strings, ao crescerem, ADICIONAM
#  caracteres à esquerda e/ou à direita delas mesmas, mas NUNCA PERDEM CARACTERES
#  NEM INSEREM CARACTERES AO MEIO.

# Gene e Gina possuem uma coleção de fotos de algumas strings durante diferentes
#  etapas de seus crescimentos. O problema é que a coleção não é rotulada, portanto
#  eles esqueceram a qual string pertence cada uma das fotos. Eles querem montar um
#  painel para ilustrar os procedimentos do cultivo de strings, mas eles necessitam 
#  sua ajuda para encontrar uma sequência de fotos apropriada.

# Cada foto ilustra uma string. A sequência de fotos precisa ter a seguinte propriedade:
#  se si aparece imediatamente antes de si+1 na sequência, então si+1 é uma string que 
#  pode ter crescido a partir de si (ou seja, si é uma substring contígua de si+1). Além
#  disso, eles não querem usar fotos repetidas, portanto todas as strings na sequência devem ser diferentes.
#  Dado um conjunto de strings representando todas as fotos disponíveis, sua tarefa é 
#  calcular o tamanho da maior sequência que pode ser produzida com as restrições acima.

# Cada caso de teste se estende por várias linhas. A primeira linha contém um inteiro N representando o
#  número de strings no conjunto (1 ≤ N ≤ 104). Cada uma das próximas N linhas contém uma string 
#  não-vazia e única com no máximo 1000 caracteres minúsculos do alfabeto inglês. Em cada caso de 
#  teste, a soma dos tamanhos das strings é no máximo 106.

# Dica: o HighLight do VS code ajuda a perceber aonde esta uma subtring no texto

# Entrada
# 6
# plant   - (depois de "an", se você escolher essa opção, PARA, nao tem como continuar, e tem tamanho 2)
# ant     - 2
# cant    - 3
# decant  - 4
# deca    - X (nao tem como sair de 'an' para 'deca', perdeu o 'n)
# an      - 1
# 2
# supercalifragilisticexpialidocious
# rag
# 0

# Saida
# 4
# 2

### Entendidmento
# É um problema semelhante a gráfico, vocÊ tem que bsucar a maior sequencia possivel que respeite o crescimento (ter toda a subparte da string anterior)
# Quem tiver mais pasos ganha e retorna o valor

# Algoritmo: Aho-Corasick

# Pode ser simplificado por: qual o maior caminho de cresciemnto para uma sequencia de strings (sempre aumenta de tamanho)

### Pilhas em Python
# Podemos utilizar as listas em Python para implementar pilhas. 
#   Para inserir um elemento no final de uma lista 
# utilizamos o método append() e para remover o elemento do topo 
#   (e atribuí-lo a uma variável) utilizamos o método pop().

# COnverter uma lsita par aum dicionario de listas onde a key é o tamanho
def sort_list_to_dict(aList):
  dict_sized = {}
  for i in aList:
    aLen = len(i)
    if(aLen not in dict_sized):
      dict_sized[aLen] = [i]
    else:
      dict_sized.append(i)
  return dict_sized

def rec_busca(aPilha, index, sort_list, dict_sized, min_size):
  # min_size = len(sort_list[index])
  list_min = []
  
  # for index1 in range(index, len(sort_list)):
  #   element = sort_list[index1]
  #   if(len(element) != min_size):
  #     break
  #   list_min.append(element)

  # Filtra
  # list(filter(lambda x: x < 0, number_list))
  q = -1
  for j in dict_sized[min_size+1]:
    if(aPilha[-1] in j):
      q = max(q , rec_busca(aPilha + j, index, sort_list, dict_sized, min_size))


def search_growth(sort_list):
  min_size = len(sort_list[0])
  list_min = []

  # for index in range(len(sort_list)):
  #   element = sort_list[index]
  #   if(len(element) != min_size):
  #     break
  #   list_min.append(element)

  dict_sized = sort_list_to_dict(sort_list)
    
  # index: o next element de size = min_size + 1
  # processa, temos so uma lista de elmetnso com sizes = min_size
  q = -1
  pilha = []
  for aElement in list_min():
    q = max(q , rec_busca([aElement], index, sort_list, dict_sized, min_size))

# TESTE: ['an', 'ant', 'cant', 'deca', 'decant', 'plant']
#        [ 1  ,   2  ,   3,  ,   -   ,     4   ,    -   ]

"""
Semelhante ao corte de haste:
1. Ordeno os elementos em um dicionário
2. Pego os elemento de menor tamanho e vou começar a recursão
  2.1. Para cada elemento de tamanho minimo eu busco o máximo que podem gerar da recursão
===> PROBLEMA: NÃO TEM SOLUÇÃO ÓTIMA VOMO A USADA EM PD
3. (Recursão):
  3.1. se 
"""

n = int(input())
while(n != 0):
  list_strings = []
  # Read Lines
  for i in range(n):
    x = input()
    if(x.isnumeric()):
        break
    else:
      list_strings.append(x)
  # Processing (Guloso)
  list_strings.sort() # ordena por tamanho da string e depois por ordem lexicografica
  print(list_strings)
  break
  n = int(input())


