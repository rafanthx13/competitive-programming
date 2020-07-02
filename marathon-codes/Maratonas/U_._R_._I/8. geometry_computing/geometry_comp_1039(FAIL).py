# Nos dias atuais uma flor de fogo não é algo considerado estranho para muitos jovens. 
#  Isso porque um famoso jogo de videogame popularizou esse tipo de flor. Nesse jogo o 
# protagonista ganhava superpoderes ao tocar em uma flor de fogo, passando a atirar 
# pequenas bolas de fogo para derrotar seus inimigos.

# No entanto, já se falava sobre flores de fogo há muito tempo atrás. Na mitologia polonesa,
#  flores de fogo são flores místicas de grande poder guardadas por espíritos malignos. 
# Ela possuía esse nome porque brilhava tanto que era impossível olhá-la diretamente. 
# Quem possuísse uma flor dessas ganharia a habilidade de ler a mente de outras pessoas,
#  encontrar tesouros escondidos e repelir todos os males.

# Para obter uma flor de fogo, a pessoa deveria procurá-la em uma floresta antes da meia-noite
#  na véspera do Noc Kupały. Exatamente à meia-noite ela floresceria. Para colhê-la seria preciso
#  desenhar um círculo em volta dela. Parece uma tarefa fácil, no entanto, os espíritos malignos 
# que guardam a flor tentariam de tudo para distrair qualquer um tentando colher a flor. 
# Se a pessoa falhasse ao tentar desenhar um círculo em volta da flor, teria sua vida sacrificada.

# Dados dois círculos, um desenhado por um ambicioso caçador de flores de fogo e outro representando 
# a área da flor, sua tarefa é determinar se o caçador morre ou fica rico com sua conquista.

# Entrada

# A entrada é composta por diversas instâncias e termina com final de arquivo (EOF). 
# Cada instância consiste em uma linha com seis inteiros, 
# R1 (1 ≤ R1) , X1(|X1|), Y1(|Y1|), R2 (R2 ≤ 1000), X2(|X2|), Y2 (Y2 ≤ 1000).
#    O círculo desenhado pelo caçador possui raio R1 e centro (X1; Y1). 
#    O círculo representando a área da flor possui raio R2 e centro (X2; Y2).

# Saída
# Para cada instância imprima uma única linha contendo MORTO, 
# se o caçador morre, ou RICO se o caçador consegue colher a flor.

# Exemplo de Entrada	Exemplo de Saída
# 6 -8 2 3 0 0        # MORTO
# 7 3 4 2 4 5         # RICO
# 3 0 0 4 0 0         # MORTO
# 5 4 7 1 8 7         # RICO


# CASO 2: 7 3 4 2 4 5 => 

#     -
#
#
#
#
#   -
#
#   $ #  |           |
#
#
#
# # # # # # # # # # # #

class Circle:

  def __init__(self, r, x, y):
      self.x = x
      self.y = y
      self.r = r

  def point_is_in(self, x, y):
    if(self.x - self.r <= x and x <= self.x + self.r):
      if(self.y - self.r <= x and x <= self.y + self.r):
        return True
    else:
      return False

  def return_four_points(self):
    return [(self.x - self.r, self.y),
            (self.x + self.r, self.y),
            (self.x, self.y - self.r),
            (self.x, self.y + self.r)]
    
while(True):
  try:

    R1, X1, Y1, R2, X2, Y2 = list(map(int, input().split()))

    hunter = Circle(R1, X1, Y1)
    flower = Circle(R2, X2, Y2)

    flag = True
    for point in flower.return_four_points():
      flag = flag and hunter.point_is_in(point[0], point[1])

    if(flag):
      print("RICO")
    else:
      print("MORTO")

  except EOFError:
    break


# 6 -8 2 3 0 0        # MORTO
# 7 3 4 2 4 5         # RICO
# 3 0 0 4 0 0         # MORTO
# 5 4 7 1 8 7         # RICO

