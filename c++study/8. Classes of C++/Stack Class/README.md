# Stack CLasse

FILO: First In, Last Out

## FUnções:

LIFO stack
Stacks are a type of container adaptor, specifically designed to operate in a LIFO context (last-in first-out), where elements are inserted and extracted only from one end of the container.

stacks are implemented as containers adaptors, which are classes that use an encapsulated object of a specific container class as its underlying container, providing a specific set of member functions to access its elements. Elements are pushed/popped from the "back" of the specific container, which is known as the top of the stack.

The underlying container may be any of the standard container class templates or some other specifically designed container class. The container shall support the following operations:
empty
size
back
push_back
pop_back

The standard container classes vector, deque and list fulfill these requirements. By default, if no container class is specified for a particular stack class instantiation, the standard container deque is used.


## Exemplo

```
/*
	Pilha - LIFO (last in first out)
*/

#include <iostream>
#include <stack>
using namespace std;

int main(int argc, char *argv[])
{
	stack<int> pilha;

	pilha.push(10);
	pilha.push(20);
	pilha.push(30);
	pilha.push(40);
	// pilha: 10, 20, 30, 40
	
	cout << "Tamanho da pilha: " << pilha.size() << endl;

	while(!pilha.empty())
	{
		int e = pilha.top();
		
		cout << e << " ";
		pilha.pop();
	}
	
	cout << "\n";

	return 0;
}

```

```
#include <iostream>  
#include <stack>  
using namespace std;  
void print_stack(stack <int> ss)  
{  
    stack <int> sg = ss;  
    while (!sg.empty())  
    {  
        cout << '\t' << sg.top();  
        sg.pop();  
    }  
    cout << '\n';  
}  
int main ()  
{  
    stack <int> newst;  
    newst.push(55);  
    newst.push(44);  
    newst.push(33);  
    newst.push(22);  
    newst.push(11);  
  
    cout << "The stack newst is : ";  
    print_stack(newst);  
    cout << "\n newst.size() : " << newst.size();  
    cout << "\n newst.top() : " << newst.top();  
    cout << "\n newst.pop() : ";  
    newst.pop();  
    newstack(newst);   
    return 0;  
}  
```