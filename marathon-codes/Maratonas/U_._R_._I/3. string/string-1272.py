# A primeira linha de entrada contém um inteiro N que indica a quantidade de casos de teste que vem a seguir.
#  Cada caso de teste consiste de uma única linha contendo de um a 50 caracteres, 
# formado por letras minúsculas (‘a’-‘z’) ou espaços (‘ ’). Atenção para possíveis espaços no início ou no final do texto!

import re

n = int(input())

for i in range(n):
  x = input()
  
  secrete = ""
  for i in x.split():
    secrete = secrete + i[0]

  print(secrete)