# Priority Queue

Ao inserir um elemento, coloca-o na posicao da fila de acordo com um valor (prioridade).

link: http://www.cplusplus.com/reference/queue/priority_queue/

## Funções
Construct priority queue (public member function )
empty
Test whether container is empty (public member function )
size
Return size (public member function )
top
Access top element (public member function )
push
Insert element (public member function )
emplace 
Construct and insert element (public member function )
pop
Remove top element (public member function )
swap 
Swap contents (public member function )

Exemplo 

```
#include <iostream>
#include <queue>
using namespace std;

int main(int argc, char *argv[]){
	priority_queue<int> pq;
	// priority_queue<int, vector<int>, greater<int> > pq; // inverte a prioridade

	pq.push(20);
	pq.push(15);
	pq.push(50);

	cout << "Elemento do topo: " << pq.top() << endl;

	if(pq.empty())
		cout << "\nFila vazia!!\n";
	else
		cout << "\nFila NAO vazia!!\n";

	cout << "\nTamanho da fila: " << pq.size() << endl;
	cout << "\nMostrando os elementos: ";

	while(!pq.empty()){
		cout << pq.top() << " ";
		pq.pop();
	}
	
	cout << endl;

	return 0;
}
``