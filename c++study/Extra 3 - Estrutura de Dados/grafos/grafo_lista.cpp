// Grafos - Lista de adjac�ncia

#include <iostream>
#include <list>
#include <algorithm> // fun��o find

using namespace std;

class Grafo
{
	int V; // n�mero de v�rtices
	list<int> *adj; // ponteiro para um array contendo as listas de adjac�ncias

public:
	Grafo(int V); // construtor
	void adicionarAresta(int v1, int v2); // adiciona uma aresta no grafo

	// obt�m o grau de sa�da de um dado v�rtice
	// grau de sa�da � o n�mero de arcos que saem de "v"
	int obterGrauDeSaida(int v);

	bool existeVizinho(int v1, int v2); // verifica se v2 � vizinho de v1
};

Grafo::Grafo(int V)
{
	this->V = V; // atribui o n�mero de v�rtices
	adj = new list<int>[V]; // cria as listas
}

void Grafo::adicionarAresta(int v1, int v2)
{
	// adiciona v�rtice v2 � lista de v�rtices adjacentes de v1
	adj[v1].push_back(v2);
}

int Grafo::obterGrauDeSaida(int v)
{
	// basta retornar o tamanho da lista que � a quantidade de vizinhos
	return adj[v].size();
}

bool Grafo::existeVizinho(int v1, int v2)
{
	if(find(adj[v1].begin(), adj[v1].end(), v2) != adj[v1].end())
		return true;
	return false;
}

int main()
{
	// criando um grafo de 4 v�rtices
	Grafo grafo(4);

	// adicionando as arestas
	grafo.adicionarAresta(0, 1);
	grafo.adicionarAresta(0, 3);
	grafo.adicionarAresta(1, 2);
	grafo.adicionarAresta(3, 1);
	grafo.adicionarAresta(3, 2);

	// mostrando os graus de sa�da
	cout << "Grau de saida do vertice 1: " << grafo.obterGrauDeSaida(1);
	cout << "\nGrau de saida do vertice 3: " << grafo.obterGrauDeSaida(3);

	// verifica se existe vizinhos
	if(grafo.existeVizinho(0, 1))
		cout << "\n\n1 eh vizinho de 0\n";
	else
		cout << "\n\n1 NAO eh vizinho de 0\n";

	if(grafo.existeVizinho(0, 2))
		cout << "2 eh vizinho de 0\n";
	else
		cout << "2 NAO eh vizinho de 0\n";

	return 0;
}
