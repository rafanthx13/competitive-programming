# A tarefa para este problema é simples: dada uma 
# lista de números, escreva o nome de cada um por extenso.

# Entrada
# A entrada consiste de uma lista de números, de tamanho 
# desconhecido (cerca de 100000 números). Haverá um único número inteiro n (0 ≤ n < 10^6) em cada linha.

# Saída
# O nome do número, por extenso, sem vírgulas (para facilitar). Preste atenção ao "e" conectivo. Veja o exemplo de saída.

# Exemplo de Entrada
# 0       zero
# 1       um
# 9       nove
# 10      dez
# 14      quatorze
# 99      noventa e nove
# 100     cem
# 101     cento e um
# 357     trezentos e cinquenta e sete
# 1000    mil
# 1001    mil e um
# 1034    mil e trinta e quatro
# 1589    mil quinhentos e oitenta e nove
# 125967  cento e vinte e cinco mil novecentos e sessenta e sete
# 10000   dez mil

d = {
  0: "zero",
  1: "um",
  2: "dois",
  3: "tres", 
  4: "quatro",
  5: "cinco",
  6: "seis",
  7: "sete",
  8: "oito",
  9: "nove",
  10: "dez",
  11: "onze",
  12: "doze",
  13: "treze",
  14: "quatorze",
  15: "quinze",
  16: "dezesseis",
  17: "dezessete",
  18: "dezoito",
  19: "dezenove",
  20: "vinte",
  30: "trinta",
  40: "quarenta",
  50: "cinquenta",
  60: "sessenta",
  70: "setenta",
  80: "oitenta",
  90: "noventa",
  100: "cento",
  200: "duzentos",
  300: "trezentos",
  400: "quatrocentos",
  500: "quinhentos",
  600: "seiscentos",
  700: "setecentos",
  800: "oitocentos",
  900: "novecentos",
  1000: "mil",
  1000000: "um milhao"
}

def form_n(num, casa):
  return ((num // casa) * casa)

# 0 a 99
def f_dezena(num):
  if(num <= 20 or num % 10 == 0):
    return str(d[num])
  else:
    return str(d[form_n(num, 10)]) + " e " + str(d[num % 10])

# 0 a 999
def f_centena(num):
  if(num < 100):
    return f_dezena(num)
  if(num == 100):
    return "cem"
  if(num % 100 == 0):
    return str(d[num])
  else:
    return  str(d[form_n(num, 100)]) + " e " + f_dezena(num % 100)

# 1000 a 999.999 = f_centena 'mil' f_centena
def f_milhar(num):
  if(num < 1000):
    return f_centena(num)
  if(num == 1000):
    return "mil"
  if(num == 100000):
    return "cem mil"
  if(num // 1000 == 1 ):
    if( num % 1000 < 100 or (num % 1000) % 100 == 0):
      return d[1000] + " e " + f_centena(num % 1000)
    else:
      return d[1000] + " " + f_centena(num % 1000)
  if(num % 1000 == 0):
    return f_centena(num // 1000) + " mil"
  else:
    
    if( num % 1000 < 100 or (num % 1000) % 100 == 0):
      return f_centena(num // 1000)  + " mil e " + f_centena(num % 1000)
    else:
      return f_centena(num // 1000)  + " mil " + f_centena(num % 1000)

lista = []

count = 0
while(True):
  try:
    n = int(input())

    if(n < 100):
      lista.append(f_dezena(n))
    elif (n < 1000):
      lista.append(f_centena(n))
    else:
      lista.append(f_milhar(n))

  except:
    break

for i in lista:
  print(i)


# HOW TODO:
#  + Esse é bem chato: ha mais regras pra fazer isso do que você possa imaginar.
#  + Quando o número é  > 1000 as vezes usa 'e' e as vezes não, ai, vocÊ pode conseiderar como sendo a exec de duas centenas

# ALGUNS EXEMPLOS
# Nove mil e três (9.003)
# Regra especial: 
# Nove mil e trinta (9.030) se nao termina com > 100, usa o e
# 66 030 = sessenta e seis mil e trinta
# 623 080 = seiscentos e vinte e três mil e oitenta

# Exemplos Muito bons, se rodar igual a isso deve rodar (100% Certo)

# 13000   treze mil
# 1300    mil e trezentos
# 130     cento e trinta
# 13      treze
# 1       um
# 13300   treze mil e trezentos
# 100300  cem mil e trezentos
# 103033  cento e tres mil e trinta e tres
# 10000   dez mil
# 1000    mil
# 1       um
# 2       dois
# 3       tres
# 4       quatro
# 5       cinco
# 6       seis
# 7       sete
# 8       oito
# 9       nove
# 10      dez
# 11      onze
# 12      doze
# 13      treze
# 14      quatorze
# 15      quinze
# 16      dezesseis
# 17      dezessete
# 18      dezoito
# 19      dezenove
# 50      cinquenta
# 60      sessenta
# 70      setenta
# 80      oitenta
# 90      noventa
# 100     cem
# 101     cento e um
# 200     duzentos
# 300     trezentos
# 400     quatrocentos
# 500     quinhentos
# 600     seiscentos
# 700     setecentos
# 800     oitocentos
# 900     novecentos
# 1000    mil