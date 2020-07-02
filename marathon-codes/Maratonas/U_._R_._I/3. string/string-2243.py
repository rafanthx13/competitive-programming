# Rolien e Naej são os desenvolvedores de um grande portal de programação. 
# Para ajudar no novo sistema de cadastro do site, eles requisitaram a sua ajuda.
#  Seu trabalho é fazer um código que valide as senhas que são cadastradas no portal, 
# para isso você deve atentar aos requisitos a seguir:

# A senha deve conter, no mínimo, 
  # uma letra maiúscula, 
  # uma letra minúscula 
  # e um número;
  # A mesma não pode ter nenhum caractere de pontuação, acentuação ou espaço;
  # Além disso, a senha pode ter de 6 a 32 caracteres.

# Entrada
  # A entrada contém vários casos de teste e termina com final de arquivo. Cada linha 
  # tem uma string S, correspondente a senha que é inserida pelo usuário no momento do cadastro.

# Saída
  # A saída contém uma linha, que pode ser “Senha valida.”, caso a senha tenha cada item 
  # dos requisitos solicitados anteriormente, ou “Senha invalida.”, se um ou mais requisitos não forem atendidos.

# Exemplo de Entrada	 Exemplo de Saída

# URI Online Judge     Senha invalida.
# AbcdEfgh99           Senha valida.
# URIOnlineJudge12     Senha valida.
# URI Online Judge 12  Senha invalida.
# Aass9                Senha invalida.
# Aassd9               Senha valida. 

while(True):
  try:
    n = input()
    flagMaiusculo = False
    flagMinusculo = False
    flagPontuacao = False
    flagNumero    = False
    if( not(len(n) >= 6 and len(n) <= 32) ):
      print("Senha invalida.")
      continue
    for i in n:
      if(i.isupper()):
        flagMaiusculo = True
      if(i.islower()):
        flagMinusculo = True
      if(i.isnumeric()):
        flagNumero = True
      if(not (i.isalpha()) and not (i.isnumeric())):
        flagPontuacao = True
    if( flagMaiusculo and flagMinusculo and flagNumero and not flagPontuacao):
      print("Senha valida.")
    else:
      print("Senha invalida.")
  except:
    break