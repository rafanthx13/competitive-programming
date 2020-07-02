# grafo-1194.py

# Fiz em C++
# REfazer em pytohn: https://gist.github.com/marcoscastro/f578862c9f27905f2653

# A primeira linha de entrada contém um número positivo C (C ≤ 2000),
#  que indica o número de casos de teste. Seguem C linhas, uma para
#  cada caso de teste. Cada caso de teste inicia com um número N (1 ≤ N ≤ 52),
#  o número de nodos da árvore binária. Depois haverá duas strings S1 e S2
#  que descrevem o percurso prefixo e infixo da árvore. Os nodos da árvore
#  são nomeados com diferentes caracteres dentro do intervalo a..z e A..Z.
#  O valor de N, S1 e S2 são separados por um espaço em branco.
#
# Saída
# Para cada conjunto de entrada, você deve imprimir uma linha contendo
# o percurso posfixo da corrente árvore.
#
# Exemplo de Entrada	Exemplo de Saída
# 3
# 3 xYz Yxz              Yzx
# 3 abc cba              cba
# 6 ABCDEF CBAEDF        CBEFDA


n = int(input())

for _ in range(n):
    entrada = input.split()
    nn = int(entrada.pop(0))
