# Set Class

Estrutura que naturalemnte nao permite elementos repeetidos

http://www.cplusplus.com/reference/set/set/

Container properties
Associative
Elements in associative containers are referenced by their key and not by their absolute position in the container.
Ordered
The elements in the container follow a strict order at all times. All inserted elements are given a position in this order.
Set
The value of an element is also the key used to identify it.
Unique keys
No two elements in the container can have equivalent keys.
Allocator-aware
The container uses an allocator object to dynamically handle its storage needs.

## FUnções

insert
Insert element (public member function )
erase
Erase elements (public member function )
swap
Swap content (public member function )
clear
Clear content (public member function )


```#include <iostream>
#include <set>
using namespace std;

int main(int argc, char *argv[])
{
	int vet[] = {70, 20, 80, 30, 40};
	set<int> myset(vet, vet + 5);

	set<int>::iterator it = myset.begin();

	cout << "\nMostrando os elementos: ";
	while(it != myset.end())
	{
		cout << *it << " ";
		it++;
	}
	
	//myset.clear();
	
	//it = myset.begin();
	//myset.erase(it);

	if(myset.empty())
		cout << "\n\nConjunto vazio!!\n";
	else
		cout << "\n\nConjunto NAO vazio!!\n";
	
	it = myset.begin();
	cout << "\nMostrando os elementos: ";
	while(it != myset.end())
	{
		cout << *it << " ";
		it++;
	}
	
	it = myset.find(70);
	if(it == myset.end())
		cout << "\n\nO elemento 70 NAO existe\n";
	else
		cout << "\n\nO elemento 70 existe\n";
	
	cout << "\nTamanho do conjunto: " << myset.size() << endl;

	return 0;
}
```