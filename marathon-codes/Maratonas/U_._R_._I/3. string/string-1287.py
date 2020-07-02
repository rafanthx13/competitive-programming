# Computadores estão presentes em uma porcentagem significante de casas pelo mundo e, 
# como programadores, somos responsáveis por criar interfaces que todos possam usar. 
# Interfaces de usuário precisam ser flexíveis de forma que se um usuário comete um
#  erro não fatal, a interface ainda pode deduzir o que o usuário queria dizer.

# Sua tarefa é escrever um programa que processe um texto de entrada representando um
# inteiro, porém, como esta é uma interface de usuário, não seremos muito rígidos com o usuário:

# 1. Se o usuário digita a letra "O" ou "o", assumimos que ele queria digitar o número "0".

# 2. Se o usuário digita a letra "l", assumimos que ele queria digitar o número "1".

# 3. Vírgulas e espaços são permitidos, porém não são processados (são ignorados).

# Se, mesmo com as regras acima, o usuário não entrou um número não-negativo, imprima a string "error". 
# Overflow (um valor maior que 2147483647) é considerado inválido e "error" deve ser impresso.

# Entrada
# Cada linha da entrada é um caso de teste e contém uma string n.

# n conterá entre 0 e 50, inclusive, letras, dígitos, espaços ou vírgulas

# Saída
# Para cada caso de teste, seu programa deverá imprimir um inteiro representado pela string 
# n ou "error" se n não é um inteiro não-negativo válido.

# Nota: Uma string vazia não representa um inteiro válido.

while(True):
  try:
    number = input()
    number = number.replace('l','1').replace('o','0').replace('O','0')
    number = number.replace(',','').replace(' ', '')
    try:
      number = int(number)
    except Exception:
      print("error")
      continue
    if(number > 2147483647):
      print("error")
    else:
      print(number)
  except EOFError:
    break