# Class Queue

Fila (FIFO) insere no fim e remove do inicio


In computer science we go for working on a large variety of programs. Each of them has their own domain and utility. Based on the purpose and environment of the program creation, we have a large number of data structures available to choose from. One of them is 'queues. Before discussing about this data type let us take a look at its syntax.

Syntax
template<class T, class Container = deque<T> > class queue;  
This data structure works on the FIFO technique, where FIFO stands for First In First Out. The element which was first inserted will be extracted at the first and so on. There is an element called as 'front' which is the element at the front most position or say the first position, also there is an element called as 'rear' which is the element at the last position. In normal queues insertion of elements take at the rear end and the deletion is done from the front.

Queues in the application areas are implied as the container adaptors.

The containers should have a support for the following list of operations:

## Lista de  funções

(constructor)	The function is used for the construction of a queue container.
empty	The function is used to test for the emptiness of a queue. If the queue is empty the function returns true else false.
size	The function returns the size of the queue container, which is a measure of the number of elements stored in the queue.
front	The function is used to access the front element of the queue. The element plays a very important role as all the deletion operations are performed at the front element.
back	The function is used to access the rear element of the queue. The element plays a very important role as all the insertion operations are performed at the rear element.
push	The function is used for the insertion of a new element at the rear end of the queue.
pop	The function is used for the deletion of element; the element in the queue is deleted from the front end.

```
#include <iostream>
#include <queue>
using namespace std;

// Exemplo de código

int main(int argc, char *argv[])
{
	queue<int> fila;

	// inserindo na fila
	fila.push(10);
	fila.push(20);
	fila.push(30);
	// fila: 10 20 30

	// mostrando o último elemento
	cout << "\nUltimo elemento: " << fila.back() << endl;

	if(fila.empty())
		cout << "\nFila vazia!!\n";
	else
		cout << "\nFila NAO vazia!!\n";

	cout << "\nPrimeiro elemento: " << fila.front() << endl;

	cout << "\nMostrando todos os elementos: ";
	
	while(!fila.empty())
	{
		int e = fila.front();
		cout << e << " ";
		fila.pop(); // remove elemento do início
	}
	
	// inserindo novamente na fila
	fila.push(10);
	fila.push(20);
	fila.push(30);
	
	cout << "\n\nTamanho da fila: " << fila.size() << endl;

	return 0;
}
```

```
#include <iostream>  
#include <queue>  
using namespace std;  
void showsg(queue <int> sg)  
{  
    queue <int> ss = sg;  
    while (!ss.empty())  
    {  
        cout << '\t' << ss.front();  
        ss.pop();  
    }  
    cout << '\n';  
}  
  
int main()  
{  
    queue <int> fquiz;  
    fquiz.push(10);  
    fquiz.push(20);  
    fquiz.push(30);  
  
    cout << "The queue fquiz is : ";  
    showsg(fquiz);  
  
    cout << "\nfquiz.size() : " << fquiz.size();  
    cout << "\nfquiz.front() : " << fquiz.front();  
    cout << "\nfquiz.back() : " << fquiz.back();  
  
    cout << "\nfquiz.pop() : ";  
    fquiz.pop();  
    showsg(fquiz);  
  
    return 0;  
}  

/*
The queue fquiz is : 	10	20	30

fquiz.size() : 3
fquiz.front() : 10
fquiz.back() : 30
fquiz.pop() : 	20	30
*/
```