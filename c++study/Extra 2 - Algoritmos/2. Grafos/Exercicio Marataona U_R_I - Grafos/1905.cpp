// https://www.urionlinejudge.com.br/judge/pt/problems/view/1905

/*
Mario adora convidar seus amigos para brincar em sua casa. 
Então decidiu convidar seus amigos para brincarem de Polícia e Ladrão. 
O jogo consiste em dois grupos, um grupo é a polícia e o outro é o grupo dos ladrões. 
Os ladrões devem se esconder e a polícia deve capturá-los. 
Caso a polícia consiga capturá-los e prendê-los os ladrões perdem o jogo e caso a 
polícia não consiga capturá-los os ladrões vencem o jogo.

Mario decidiu que seria do grupo da polícia e que teria que procurar seus 
amigos do grupo dos ladrões e capturá-los, porém algum de seus amigos 
sentiram-se em desvantagens por não possuírem lugares estratégicos para 
se esconder no seu quintal.

Portanto decidiram planejar uma forma em que poderiam deixar os policiais 
sem saída e terem chances de ganhar o jogo. Para isso montaram um labirinto 
usando caixas de papelão e marcaram como “0” todos os lugares no quintal 
aonde os policiais poderiam atravessar e como “1” aonde os policiais não 
poderiam atravessar.

Os ladrões irão se esconder sempre no último espaço do labirinto, 
Se os policiais ficarem encurralados no labirinto os ladrões vencem 
e poderão comemorar a fuga, mas se os policiais alcançarem o ultimo 
espaço do labirinto os policiais serão os vencedores. Os policiais 
poderão andar somente nos blocos marcados como 0. Sua tarefa é determinar 
a partir do labirinto quem vai ganhar o jogo.

Exemplo de Entrada	Exemplo de Saída
2
 
0 0 0 0 1           ==> COPS
1 1 0 0 1
0 1 0 0 0
0 0 0 1 1
1 1 0 0 0
 
0 0 0 0 1           ==> ROBBERS
1 1 0 0 1
0 1 0 0 0
0 0 1 1 1
1 1 0 0 0 

*/

/*
Resolução: 
+ A partir do primeira quadrado [0,0] deve chegar a [5,5]
+ A ideia é fazer por grafo, e será sem usar nenhum algorimo especifico. 
    Vai fazer uma busca e marcar os locais que já foram marcados

*/

#include <iostream>
#include <vector>

using namespace std;

class Coordenada {
  public:
    int x, y;
    bool visitada;
};

int winner; // global

/*
  Vai realisar diversas buscar até encontrar. (setando em 1) se nao
  , passa por todos os casos e nao faz nada (continua 0 e termina)
*/

void busca(vector < vector <int> > mat, vector< vector <Coordenada> > coordenadas, int i, int j) {
  if (i >= 0 && i < 5 && j >= 0 && j < 5 && !winner) {
    coordenadas[i][j].visitada = true; // seta que foi visitada
    if (i == 4 && j == 4)
      winner = 1;
    else {
      // vai para baixo, cima, esquerda ou direita
      if (i + 1 < 5 && mat[i + 1][j] == 0 && !coordenadas[i + 1][j].visitada)
        busca(mat, coordenadas, i + 1, j);
      if (i - 1 >= 0 && mat[i - 1][j] == 0 && !coordenadas[i - 1][j].visitada)
        busca(mat, coordenadas, i - 1, j);
      if (j + 1 < 5 && mat[i][j + 1] == 0 && !coordenadas[i][j + 1].visitada)
        busca(mat, coordenadas, i, j + 1);
      if (j - 1 >= 0 && mat[i][j - 1] == 0 && !coordenadas[i][j - 1].visitada)
        busca(mat, coordenadas, i, j - 1);
    }
  }
}

int main(int argc, char * argv[]) {
  int T;

  cin >> T;

  for (int i = 0; i < T; i++) {
    vector < vector < int > > mat(5);
    vector < vector < Coordenada > > coordenadas(5);
    for (int j = 0; j < 5; j++) {
      mat[j].resize(5);
      coordenadas[j].resize(5);
    }

    for (int j = 0; j < 5; j++) {
      for (int k = 0; k < 5; k++) {
        int e;
        cin >> e;
        mat[j][k] = e;

        coordenadas[j][k].x = j;
        coordenadas[j][k].y = k;
        coordenadas[j][k].visitada = false;
      }
    }

    winner = 0;
    busca(mat, coordenadas, 0, 0);

    if (winner)
      cout << "COPS\n";
    else
      cout << "ROBBERS\n";
  }

  return 0;
}