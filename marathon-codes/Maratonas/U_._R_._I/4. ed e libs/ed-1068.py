# a+(b*c)-2-a        está correto
# (a+b*(2-c)-2+a)*2  está correto

# enquanto

# (a*b-(2+c)         está incorreto
# 2*(3-a))           está incorreto
# )3+b*(2-c)(        está incorreto

# Ou seja, todo parênteses que fecha deve ter um outro parênteses 
# que abre correspondente e não pode haver parênteses que fecha sem um 
# previo parenteses que abre e a quantidade total de parenteses que abre e fecha deve ser igual.

# Entrada
# Como entrada, haverá N expressões (1 <= N <= 10000), cada uma delas com até 1000 caracteres.

# Saída
# O arquivo de saída deverá ter a quantidade de linhas correspondente ao arquivo de entrada, 
# cada uma delas contendo as palavras correct ou incorrect de acordo com as regras acima fornecidas.

# a+(b*c)-2-a 
# (a+b*(2-c)-2+a)*2 
# (a*b-(2+c) 
# 2*(3-a))  
# )3+b*(2-c)( 

# correct
# correct
# incorrect
# incorrect
# incorrect


# Solução: 
# Usar pilha, a pilha deve-se empilhar e desempilhar numa certa ordem e, no final, deve está vazia.
# append() para dar o push() e pop para dar pop() que retorno o ultimo elemento



while(True):
  try:
    exp = input()
    queue = []
    flag = False

    for w in exp:
      if(w == '('):
        queue.append(w)
      elif(w == ')'):
        if(not queue):
          flag = True
          continue
        lastItem = queue.pop()
        if(lastItem != '('):
          flag = True
          continue

    
    if(flag):
       print('incorrect')
       continue

    if(not queue):
      print("correct")
    else:
      print('incorrect')
  except EOFError:
    break