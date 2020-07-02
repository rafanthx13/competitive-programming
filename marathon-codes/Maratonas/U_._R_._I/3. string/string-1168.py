# Entrada
  # 3
    # 115380
    # 2819311
    # 23456

# Saida
  # 27 leds
  # 29 leds
  # 25 leds

dict_leds = {
  1 : 2,
  2 : 5,
  3 : 5,
  4 : 4,
  5 : 5,
  6 : 6,
  7 : 3,
  8 : 7,
  9 : 6,
  0 : 6
}

lista = []

n = int(input())

for i in range(n):
  x = input()
  sun = 0
  for j in range(len(x)):
    sun = sun + dict_leds[int(x[j])]
  lista.append(sun)

for k in lista:
  print(k, "leds")
