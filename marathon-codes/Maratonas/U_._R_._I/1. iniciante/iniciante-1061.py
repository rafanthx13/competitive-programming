# URI - Diferença de Tempo - 04/06/2019 - ACCEPT

# Dia 5
# 08 : 12 : 23

# Dia 9
# 06 : 13 : 23

# 3 dia(s)
# 22 hora(s)
# 1 minuto(s)
# 0 segundo(s)

SPLITED = " : "

def tempo_passado(h,m,s):
    return h*60*60 + m*60 + s

def tempo_inverso(x):
    return 86400 - x

def list_time(segundos):
  dias = segundos // 86400
  horas = (segundos % 86400) // 3600
  minutos = ((segundos % 86400) % 3600) // 60
  segundos = ((segundos % 86400) % 3600) % 60
  return [dias, horas, minutos, segundos]

dia1 = input().split()[1]
h1 = input().split(SPLITED)
dia2 = input().split()[1]
h2 = input().split(SPLITED)

diff_dias = int(dia2) - int(dia1)

tempo_final_segundos = 0

x = tempo_passado(int(h1[0]), int(h1[1]), int(h1[2]))
y = tempo_passado(int(h2[0]), int(h2[1]), int(h2[2]))

if(diff_dias == 0):
  tempo_final_segundos = y - x

if(diff_dias == 1):
  tempo_final_segundos = tempo_inverso(x) + y

if(diff_dias > 1):
  tempo_final_segundos = tempo_inverso(x) + y  + ((diff_dias - 1) * 86400)

l = list_time(tempo_final_segundos)

print(l[0], "dia(s)")
print(l[1], "hora(s)")
print(l[2], "minuto(s)")
print(l[3], "segundo(s)")