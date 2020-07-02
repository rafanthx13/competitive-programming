#ifndef _LISTA_H_
#define _LISTA_H_

// Definindo uma TAD Lista encadead com Classe usando Template para podermos criarmos de qualquer tipo

using namespace std;

// classe No
template<class T>
class No {

private:
	T v;
	No* prox;

public:
	No(T v) // construtor
	{
		this->v = v;
		this->prox = NULL;
	}

	T obterValor() // obt�m o valor
	{
		return v;
	}

	No* obterProx() // obt�m o pr�ximo No
	{
		return prox;
	}

	void setProx(No* p) // seta o pr�ximo No
	{
		prox = p;
	}
};

// classe Lista
template<class T>
class Lista
{
private:
	No<T> *cabeca; // primeiro elemento
	No<T> *cauda; // �ltimo elemento

public:
	Lista()
	{
		// se n�o passar elemento, ent�o cabeca e cauda s�o NULL
		cabeca = NULL;
		cauda = NULL;
	}

	Lista(T v)
	{
		// se passar elemento, ent�o cria novo No
		cabeca = new No<T>(v);
		cauda = cabeca;
	}

	virtual ~Lista() // destrutor
	{
		delete cabeca;
	}

	void mostrar() // mostra todos os elementos da lista
	{
		cout << "\nImprimindo todos os elementos...\n";
		No<T>* c = cabeca;

		if(vazia())
			cout << "A lista NAO possui elementos!!\n";
		else
		{
			while(c) // percorre a lista
			{
				cout << c->obterValor() << endl;
				c = c->obterProx();
			}
			cout << endl;
		}
	}

	bool vazia() // verifica se a lista est� vazia
	{
		return (cabeca == NULL);
	}

	// insere no in�cio (semelhante a push_front da list)
	void inserir_inicio(T v)
	{
		No<T>* novo_no = new No<T>(v);

		novo_no->setProx(cabeca);
		cabeca = novo_no;
	}

	// insere no final (semelhante a push_back da list)
	void inserir_final(T v)
	{
		No<T>* novo_no = new No<T>(v);

		if(vazia())
		{
			cabeca = novo_no;
			cauda = novo_no;
		}
		else
		{
			cauda->setProx(novo_no);
			cauda = novo_no;
		}
	}

	// retorna o tamanho da lista
	int tamanho()
	{
		if(vazia()) // se for vazia, ent� retorna 0
			return 0;

		No<T>* c = cabeca;
		int tam = 0;
		
		// percorre a lista
		do
		{
			c = c->obterProx();
			tam++;
		}
		while(c);
		
		return tam;
	}

	// verifica se um elemento existe na lista
	bool existe(int v)
	{
		No<T>* c = cabeca;
		
		while(c)
		{
			if(c->obterValor() == v)
				return true;
			c = c->obterProx();
		}
		return false;
	}

	// remove da lista, remo��o do final (semelhante a pop_back da list)
	void remover()
	{
		if(!vazia())
		{
			// se houver s� 1 elemento
			if(cabeca->obterProx() == NULL)
				cabeca = NULL;
			else if(cabeca->obterProx()->obterProx() == NULL) // 2 elementos
				cabeca->setProx(NULL);
			else // > 2 elementos
			{
				No<T>* ant_ant = cabeca;
				No<T>* ant = cabeca->obterProx();
				No<T>* corrente = cabeca->obterProx()->obterProx();

				while(corrente)
				{
					No<T>* aux = ant;
					ant = corrente;
					ant_ant = aux;
					corrente = corrente->obterProx();
				}
				delete ant_ant->obterProx(); // libera mem�ria
				ant_ant->setProx(NULL); // seta o prox como NULL
				cauda = ant_ant; // atualiza a cauda
			}
		}
	}
};

#endif