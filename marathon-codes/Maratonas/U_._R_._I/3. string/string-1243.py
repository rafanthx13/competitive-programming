# string 1243

# Se o comprimento médio das palavras do enunciado é menor ou igual a 3, 
  # o problema recebe dificuldade de 250 pontos.
# Se o comprimento médio das palavras do enunciado for 4 ou 5, 
  # o problema recebe dificuldade de 500 pontos. 
# Se o comprimento médio das palavras do enunciado for maior ou igual a 6,
  # o problema recebe dificuldade de 1000 pontos.

def copy_string(string):
  s = ""
  for i in string:
    s = s + i
  return s

def isAWord(string):
  splited = copy_string(string).split()
  listaPalavras = []
  # verifica para cada palavra ad lista se sao valiads ou nao
  for indexWord in range(len(splited)):
    isWordFlag = True
    aWord = splited[indexWord]
    # verifica se tem numero, se tiver, sera false
    for i in range(len(aWord)):
      c = aWord[i]
      if( (not c.isalpha() and c != " " and c != ".") or (c == "." and i != (len(aWord) -1)) ): 
        isWordFlag = False
        break
    # checka a word
    if(isWordFlag):
      listaPalavras.append(aWord)
  # Retornara uma lista das palavras validas
  return listaPalavras

def filter_points(alist):
  l = []
  for i in alist:
    l.append(i.replace(".",""))
  return l

alistV = []

count = 0

while(True):
    try:
      x = input()
      
      q = 0
      lista = filter_points(isAWord(x))
      for j in lista:
        q = q + len(j)
      qtd = len(lista)

      v = 0

      media = 0 if(q == 0 or qtd == 0) else q // qtd

      if(media <= 3):
        v = 250
      if(media > 3 and media < 6):
        v = 500
      if(media >= 6):
        v = 1000
      

      print(v)
        
    except EOFError:
        break
