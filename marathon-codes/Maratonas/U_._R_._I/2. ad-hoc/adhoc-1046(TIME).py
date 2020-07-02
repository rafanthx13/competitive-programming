# 6+9=15 parece ok. Mas como pode estar certo 4+6=2?

# Veja só. Mofiz trabalhou duro durante seu curso de Eletrônica Digital, 
# mas quando lhe foi solicitado que implementasse um somador de 32 bits 
# como exame no laboratório, ele acabou fazendo algum erro na parte de projeto. 
# Depois de vasculhar seu projeto por uma hora e meia, ele encontrou seu erro. 
# Ele estava fazendo soma de bits, mas seu carregador de bit (carry) 
# sempre apresentava como saída o valor zero. Portanto,

# 4  = 00000000 00000000 00000000 00000100
# +6 = 00000000 00000000 00000000 00000110
# ----------------------------------------
# 2  = 00000000 00000000 00000000 00000010


# Claro que já é uma boa coisa ele finalmente ter encontrado o seu erro, 
# mas isso foi muito tarde. Considerando seu esforço durante o curso, o 
# instrutor deu a ele mais uma chance: Mofiz teria que escrever um programa
#  eficiente que pegaria 2 valores decimais de 32 bits sem sinal como entrada 
# e deveria produzir um número de 32 bits sem sinal como saída, ou seja, 
# somando do mesmo modo como o circuito faz.

# Entrada
  # Em cada linha de entrada haverá um par de inteiros 
  # separado por um único espaço. A entrada termina com EOF.

# Saída
  # Para cada linha de entrada, o programa deverá fornecer uma linha de saída,
  #  que é o valor após somar dois números no modo “Mofiz”.

# Exemplo de Entrada	  Exemplo de Saída
# 4 6                   2
# 6 9                   15

# 4 = 00000100
# 6 = 00000110
# 2 = 00000010

# def int_to_bin(n):
#   return '{0:032b}'.format(n)

while(True):
  try:
    a, b = list(map(int, input().split()))
    aa = '{0:032b}'.format(a)
    bb = '{0:032b}'.format(b)
    r = ''
    # print(aa, bb)
    for i in range(32):
      r = r + str( (int(aa[31-i]) + int(bb[31-i])) % 2 )
    print( int(''.join(reversed(r)), 2) ) # [::-1] => inverte a string
    # ''.join(reversed(str))
  except EOFError:
    break

# 1 1                    0
# 1 2                    3
# 2 2                    0
# 2 3                    1
# 3 3                    0
# 4 1                    5
# 1 4                    5
# 10 10                  0
# 21 10                  31
# 21 14                  27
# 123 321                314 => 219
# 0 0                    0
# 2863311530 1431655765  4294967295
# 4294967295 4294967295  0