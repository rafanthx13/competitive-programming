[h1, m1, h2, m2] = list(map(int, input().split()))

# 7:10 --> 8:09 => 59

inicio = m1 + 60*h1
fim = m2 + 60*h2
# print("1:", inicio)
# print("2:", fim)
diff = fim - inicio

if(diff < 0):
    diff = 24*60 - abs(diff)

# print("diff:", diff)

if(diff <= 59):
    horas = 0
    minutos = diff
elif(diff == 0):
    horas = 24
    minutos = 0
else:
    horas = diff // 60
    minutos = diff % 60

if(diff == 0):
    horas = 24
    minutos = 0

print("O JOGO DUROU", horas, "HORA(S) E", minutos, "MINUTO(S)")
