# Class Map

É o dicionário do Python, porem mais tipado: tanto a chave quanto o valor tem que ser de um tipo fixo

COmo usar 

```
#include <map>   
using namespace std;  
int main()  
{  
   map<int, string> Employees;    // mapa que recebe numero e mapeia para strings
   Employees[101] = "Nikita";  

```

```
#include <string.h>  
#include <iostream>  
#include <map>  
#include <utility>  
using namespace std;  
int main()  
{  
   map<int, string> Employees;  
   // 1) Assignment using array index notation  
   Employees[101] = "Nikita";  
   Employees[105] = "John";  
   Employees[103] = "Dolly";  
   Employees[104] = "Deep";  
   Employees[102] = "Aman";  
   cout << "Employees[104]=" << Employees[104] << endl << endl;  
   cout << "Map size: " << Employees.size() << endl;  
   cout << endl << "Natural Order:" << endl;  
   for( map<int,string>::iterator ii=Employees.begin(); ii!=Employees.end(); ++ii)  
   {  
       cout << (*ii).first << ": " << (*ii).second << endl;  
   }  
   cout << endl << "Reverse Order:" << endl;  
   for( map<int,string>::reverse_iterator ii=Employees.rbegin(); ii!=Employees.rend(); ++ii)  
   {  
       cout << (*ii).first << ": " << (*ii).second << endl;  
   }  
}  
```

insert	Insert element in the map.
erase	Erase elements from the map.
swap	Exchange the content of the map.
clear	Delete all the elements of the map.
emplace	Construct and insert the new elements into the map.
emplace_hint	Construct and insert new elements into the map by hint.

## Há tambem o MultiMap

https://www.geeksforgeeks.org/multimap-associative-containers-the-c-standard-template-library-stl/

ELe permite que uma mesma chave tenha mais um elemento, como no exempo a baixo


```
#include <iostream> 
#include <map> 
#include <iterator> 
  
using namespace std; 
  
int main() { 
    multimap <int, int> gquiz1;        // empty multimap container 
  
    // insert elements in random order 
    gquiz1.insert(pair <int, int> (1, 40)); 
    gquiz1.insert(pair <int, int> (2, 30)); 
    gquiz1.insert(pair <int, int> (3, 60)); 
    gquiz1.insert(pair <int, int> (4, 20)); 
    gquiz1.insert(pair <int, int> (5, 50)); 
    gquiz1.insert(pair <int, int> (6, 50)); 
    gquiz1.insert(pair <int, int> (6, 10)); 
  
    // printing multimap gquiz1 
    multimap <int, int> :: iterator itr; 
    cout << "\nThe multimap gquiz1 is : \n"; 
    cout << "\tKEY\tELEMENT\n"; 
    for (itr = gquiz1.begin(); itr != gquiz1.end(); ++itr) { 
        cout  <<  '\t' << itr->first <<  '\t' << itr->second << '\n'; 
    } 
    cout << endl; 

}

/* OutPut
The multimap gquiz1 is : 
    KEY    ELEMENT
    1    40
    2    30
    3    60
    4    20
    5    50
    6    50
    6    10
*/
```
