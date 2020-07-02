# Implemente um programa denominado combinador, que recebe duas strings 
# e deve combiná-las, alternando as letras de cada string, começando com
#  a primeira letra da primeira string, seguido pela primeira letra da s
# egunda string, em seguida pela segunda letra da primeira string, e 
# assim sucessivamente. As letras restantes da cadeia mais longa devem 
# ser adicionadas ao fim da string resultante e retornada.

# Entrada
# A entrada contém vários casos de teste. A primeira linha contém um inteiro
#  N que indica a quantidade de casos de teste que vem a seguir. Cada caso de
#  teste é composto por uma linha que contém duas cadeias de caracteres, cada 
# cadeia de caracteres contém entre 1 e 50 caracteres inclusive.

# Saída
# Combine as duas cadeias de caracteres da entrada como mostrado no exemplo abaixo e exiba a cadeia resultante.

# Exemplo de Entrada	Exemplo de Saída
# 2
# Tpo oCder
# aa bb

# TopCoder
# abab

n = int(input())

for i in range(n):
  w = input()
  lista = w.split()
  ww = ''
  if(len(lista[0]) > len(lista[1])):
    menorlen = len(lista[1])
    maior = lista[0]
  else:
    menorlen = len(lista[0])
    maior = lista[1]

  for i in range(menorlen):
    ww = ww + lista[0][i]
    ww = ww + lista[1][i]

  ww = ww + maior[menorlen:]
  print(ww)