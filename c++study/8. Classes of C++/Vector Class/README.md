# Class Vector of C++

link: https://www.javatpoint.com/cpp-vector

A vector is a sequence container class that implements dynamic array, means size automatically changes when appending elements. A vector stores the elements in contiguous memory locations and allocates the memory as needed at run time.

Difference between vector and array
An array follows static approach, means its size cannot be changed during run time while vector implements dynamic array means it automatically resizes itself when appending elements.

voce importa com `#include<vector>` e cria o `vector` para ter um determinado tipo. EM seguida você pode mainulalao como um array dinmaico, sem tamanho definido, colocando elesmentos desse tipo.

OBs: Vetor tem acesso rápido,mas é ruim se você acabar removendo elemento deles. A remoçâo de um elemento implica em arrastar várias elemetnos. Uma outra opçâo seria list. INserir e remover elemtnos custa, a nao ser que adicione e remova do final. 



exemplo:
```
#include<iostream>  
#include<vector>  
using namespace std;  
int main()  
{  
vector<string> v1;  
v1.push_back("javaTpoint ");  
v1.push_back("tutorial");  
for(vector<string>::iterator itr=v1.begin();itr!=v1.end();++itr)  
cout<<*itr;  
return 0;   
}  

```

#### FUnções

at()	It provides a reference to an element.
back()	It gives a reference to the last element.
front()	It gives a reference to the first element.
swap()	It exchanges the elements between two vectors.
push_back()	It adds a new element at the end.
pop_back()	It removes a last element from the vector.
empty()	It determines whether the vector is empty or not.
insert()	It inserts new element at the specified position.
erase()	It deletes the specified element.
resize()	It modifies the size of the vector.
clear()	It removes all the elements from the vector.
size()	It determines a number of elements in the vector.
capacity()	It determines the current capacity of the vector.
assign()	It assigns new values to the vector.
operator=()	It assigns new values to the vector container.
operator[]()	It access a specified element.
end()	It refers to the past-lats-element in the vector.
emplace()	It inserts a new element just before the position pos.
emplace_back()	It inserts a new element at the end.
rend()	It points the element preceding the first element of the vector.
rbegin()	It points the last element of the vector.
begin()	It points the first element of the vector.
max_size()	It determines the maximum size that vector can hold.
cend()	It refers to the past-last-element in the vector.
cbegin()	It refers to the first element of the vector.
crbegin()	It refers to the last character of the vector.
crend()	It refers to the element preceding the first element of the vector.
data()	It writes the data of the vector into an array.
shrink_to_fit()	It reduces the capacity and makes it equal to the size of the vector.

### Iterando

it é o interarot

```
  vector<Ponto*> vet;
	vector<Ponto*>::iterator it;

	Ponto* p1 = new Ponto(1, 2);
	Ponto* p2 = new Ponto(3, 4);

	vet.push_back(p1);
	vet.push_back(p2);
 
	for(it = vet.begin(); it != vet.end(); it++)
		cout << "(" << (*it)->x << ", " << (*it)->y << ")\n";
  ```