# List Class

lnik:
+ https://www.javatpoint.com/post/cpp-list

### Desempenho da lista

+ Bom para bastante adiçâo e remoção, pois tem custo O(1), enquanto que Vetor custa O(n)
+ Não tem acesso alertotiro, ou seja, se vocẽ quiser busca o elemetno de posicao t, vai gasata n paso para chegar la, enquanto que no vetor é mai rápdio

template de lista

```
#include<iostream>  
#include<list>  
using namespace std;  
int main()  
{  
   list<int> l;  
}
```

## FUnçoes

insert()	It inserts the new element before the position pointed by the iterator.
push_back()	It adds a new element at the end of the vector.
push_front()	It adds a new element to the front.
pop_back()	It deletes the last element.
pop_front()	It deletes the first element.
empty()	It checks whether the list is empty or not.
size()	It finds the number of elements present in the list.
max_size()	It finds the maximum size of the list.
front()	It returns the first element of the list.
back()	It returns the last element of the list.
swap()	It swaps two list when the type of both the list are same.
reverse()	It reverses the elements of the list.
sort()	It sorts the elements of the list in an increasing order.
merge()	It merges the two sorted list.
splice()	It inserts a new list into the invoking list.
unique()	It removes all the duplicate elements from the list.
resize()	It changes the size of the list container.
assign()	It assigns a new element to the list container.
emplace()	It inserts a new element at a specified position.
emplace_back()	It inserts a new element at the end of the vector.
emplace_front()	It inserts a new element at the beginning of the list.