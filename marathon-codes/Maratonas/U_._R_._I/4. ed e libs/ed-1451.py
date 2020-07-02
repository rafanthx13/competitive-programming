# Você está digitando um texto longo com um teclado quebrado. 
# Bem, não tão quebrado. O único problema com o teclado é que 
# às vezes a tecla "home" ou a tecla "end" é automaticamente 
# pressionada (internamente). Você não está ciente deste problema, 
# já que você está focado no texto e nem sequer ligou o monitor! 
# Depois que você terminar de digitar, você pode ver um texto na tela
#  (se você ligar o monitor). Em chinês, podemos chamar este texto de Beiju. 
# Sua tarefa é encontrar o texto Beiju.

# Entrada
# Há diversos casos de teste. Cada teste é uma única linha que contém pelo 
# menos uma e, no máximo, 100.000 letras, underscores e dois caracteres especiais 
# '[' e ']'. '[' Significa que a tecla "Home" é pressionada internamente, e ']' 
# significa que a tecla "End" é pressionada internamente. A entrada é terminada 
# por fim de arquivo (EOF). O tamanho do arquivo de entrada não excede 5MB.

# Saída
# Para cada caso, imprimir o texto Beiju na tela.

# Exemplo de Entrada	Exemplo de Saída
# This_is_a_[Beiju]_text
# [[]][]Happy_Birthday_Tsinghua_University

# BeijuThis_is_a__text
# Happy_Birthday_Tsinghua_University

while(True):
  try:
    s = input()
    ss = []
    pilha = []
    c = 0
    r_a = []
    r_b = []
    for w in s:
      if(w == '['):
        r_a.append(c)
      elif(w == ']'):
        r_b.append(c)
        pilha.append((r_a.pop(), r_b.pop()))
      c += 1

      for par in pilha[::-1]:
        s = s

  except EOFError:
    break