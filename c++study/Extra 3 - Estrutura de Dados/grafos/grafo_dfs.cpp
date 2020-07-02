// Grafos - DFS (busca em profundidade)

#include <iostream>
#include <list>
#include <algorithm> // fun��o find
#include <stack> // pilha para usar na DFS

using namespace std;

class Grafo {
  int V; // n�mero de v�rtices
  list < int > * adj; // ponteiro para um array contendo as listas de adjac�ncias

  public:
    Grafo(int V); // construtor
  void adicionarAresta(int v1, int v2); // adiciona uma aresta no grafo

  // faz uma DFS a partir de um v�rtice
  void dfs(int v);
};

Grafo::Grafo(int V) {
  this->V = V; // atribui o n�mero de v�rtices
  adj = new list < int > [V]; // cria as listas
}

void Grafo::adicionarAresta(int v1, int v2) {
  // adiciona v�rtice v2 � lista de v�rtices adjacentes de v1
  adj[v1].push_back(v2);
}

void Grafo::dfs(int v) {
  stack < int > pilha;
  bool visitados[V]; // vetor de visitados

  // marca todos como n�o visitados
  for (int i = 0; i < V; i++)
    visitados[i] = false;

  while (true) {
    if (!visitados[v]) {
      cout << "Visitando vertice " << v << " ...\n";
      visitados[v] = true; // marca como visitado
      pilha.push(v); // insere "v" na pilha
    }

    bool achou = false;
    list < int > ::iterator it;

    // busca por um vizinho n�o visitado
    for (it = adj[v].begin(); it != adj[v].end(); it++) {
      if (!visitados[ * it]) {
        achou = true;
        break;
      }
    }

    if (achou)
      v = * it; // atualiza o "v"
    else {
      // se todos os vizinhos est�o visitados ou n�o existem vizinhos
      // remove da pilha
      pilha.pop();
      // se a pilha ficar vazia, ent�o terminou a busca
      if (pilha.empty())
        break;
      // se chegou aqui, � porque pode pegar elemento do topo
      v = pilha.top();
    }
  }
}

int main() {
  int V = 8;

  Grafo grafo(V);

  // adicionando as arestas
  grafo.adicionarAresta(0, 1);
  grafo.adicionarAresta(0, 2);
  grafo.adicionarAresta(1, 3);
  grafo.adicionarAresta(1, 4);
  grafo.adicionarAresta(2, 5);
  grafo.adicionarAresta(2, 6);
  grafo.adicionarAresta(6, 7);

  grafo.dfs(0);

  return 0;
}