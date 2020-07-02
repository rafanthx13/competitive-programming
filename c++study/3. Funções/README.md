## FUnções

sintaxe da definiçao de uma funçao

return_type function_name( parameter list ) {
   body of the function
}

Exemplo

```
int max(int num1, int num2) {
   // local variable declaration
   int result;
 
   if (num1 > num2)
      result = num1;
   else
      result = num2;
 
   return result; 
}


```

sinxtaxe da declaraçao de uma funçaoi

return_type function_name( parameter list );

For the above defined function max(), following is the function declaration −

int max(int num1, int num2);
Parameter names are not important in function declaration only their type is required, so following is also valid declaration −

int max(int, int);

+++++++++++++++++++++=

SOBRE CARGA DE FUNÇÃO
O que diferencia uma funão da outra é: o número de parametros e os tipos dos parametros, (na ordem). Se mudar qualquer uma dessas coisa, havera sobrecarga.

```
#include <iostream>

using namespace std;

int soma(int n1, int n2)
{
	return n1 + n2;
}

int soma(int n1, int n2, int n3)
{
	return n1 + n2 + n3;
}

int main(int argc, char *argv[])
{
	cout << soma(1, 2) << endl;
	cout << soma(1, 2, 3) << endl;
	return 0;
}
```





++++++++++++++++++=

DEPOIS QUE VER PONTEIRO VOLTE A ESE LINK

https://www.tutorialspoint.com/cplusplus/cpp_functions.htm

E BUS QUE NO FINAL chamar a funçao por referencia/valor/ponteiro

+++++++++++++++++++++

# módulos

links:
+ https://docs.microsoft.com/pt-br/cpp/cpp/header-files-cpp?view=vs-2019
+ http://www.cplusplus.com/forum/articles/10627/

## COnselhos de uso de módu,los

Como um arquivo de cabeçalho potencialmente pode ser incluído por vários arquivos, ele não pode conter definições que podem produzir várias definições de mesmo nome. O exemplo a seguir não é permitidas ou é considerados muito boa prática:

+ definições de tipo interno no namespace ou escopo global
+ definições de função não embutida
+ definições de variável não const
+ definições de agregação
+ namespaces sem nome
+ usando diretivas

Usar o usando diretiva não necessariamente causará um erro, mas potencialmente pode causar um problema porque ele traz o namespace no escopo em todos os arquivos. cpp que direta ou indiretamente, inclua esse cabeçalho.

devem ser declaradaos da seguinte forma

O ARQUVIO HEADER, É BOM FAZELO PARA SEGUIR COMO ESSA EXTRUTURA
arquivo.h
```
//=================================
// include guard
#ifndef __MYCLASS_H_INCLUDED__
#define __MYCLASS_H_INCLUDED__

//=================================
// forward declared dependencies
class Foo;
class Bar;

//=================================
// included dependencies
#include <vector>
#include "parent.h"

//=================================
// the actual class
class MyClass : public Parent  // Parent object, so #include "parent.h"
{
public:
  std::vector<int> avector;    // vector object, so #include <vector>
  Foo* foo;                    // Foo pointer, so forward declare Foo
  void Func(Bar& bar);         // Bar reference, so forward declare Bar

  friend class MyFriend;       // friend declaration is not a dependency
                               //   don't do anything about MyFriend
};

#endif // __MYCLASS_H_INCLUDED__ 
```

## Exemplo

main.cpp
```
#include <iostream>
#include "my_math.h"

using namespace std;

int main(int argc, char *argv[])
{
	int n = 5;

	cout << "Fatorial de " << n << ": " << fatorial(5) << endl;
	cout << "Quadrado com lado " << n << ": " << area_quadrado(5) << endl;
	cout << "Area retangulo " << area_retangulo(5, 5) << endl;
	return 0;
}

```

my_math.h
```
#ifndef _MY_MATH_H_
#define _MY_MATH_H_

int fatorial(int n);
int area_quadrado(int lado);
int area_retangulo(int altura, int base);

#endif
```

my_math.cpp
```
/* Esse m�dulo cont�m fun��es matem�ticas */

int fatorial(int n)
{
	int fat = 1;

	for(int i = 1; i < n; i++)
		fat = fat * (i + 1);
	return fat;
}

int area_quadrado(int lado)
{
	return lado * lado;
}

int area_retangulo(int altura, int base)
{
	return altura * base;
}

```

## Escopo

### escopo global
+ Quando você colocar a variavel foram da main, ai ela se torna global e pode acessar em qualquwe lugar como uma variaǘel normal

### variavel estatica

+ Mesmo definindo ela denovo ela nao é recirada, passa pelo codigo e nao faz nada
+ Util para saber por exmeplo, quantas veses uma funçâo é chamada


https://www.tutorialspoint.com/cplusplus/cpp_storage_classes.htm

The static storage class instructs the compiler to keep a local variable in existence during the life-time of the program instead of creating and destroying it each time it comes into and goes out of scope. Therefore, making local variables static allows them to maintain their values between function calls.

The static modifier may also be applied to global variables. When this is done, it causes that variable's scope to be restricted to the file in which it is declared.

In C++, when static is used on a class data member, it causes only one copy of that member to be shared by all objects of its class.

```
#include <iostream>
 
// Function declaration
void func(void);
 
static int count = 10; /* Global variable */
 
main() {
   while(count--) {
      func();
   }
   
   return 0;
}

// Function definition
void func( void ) {
   static int i = 5; // local static variable
   i++;
   std::cout << "i is " << i ;
   std::cout << " and count is " << count << std::endl;
}
```
Saida
```
i is 6 and count is 9
i is 7 and count is 8
i is 8 and count is 7
i is 9 and count is 6
i is 10 and count is 5
i is 11 and count is 4
i is 12 and count is 3
i is 13 and count is 2
i is 14 and count is 1
i is 15 and count is 0
```

##### Argumentos da funçâo main






##### Prametros default

COm ele, a pessoa nao precisa pasaara um ou mais paramteores.Para fazer, basta comlocar o = na sua definiçâo

```
Carro(int ano = 2014)
```

### inline function

basta colocar a keyword `inline` na frete.

lnik: http://www.tiexpert.net/programacao/c/funcoes-inline.php

Funções inline
As funções inline servem como códigos a serem copiados ao lugar que são chamados.

Funções normais quando são chamadas, o programa tem que ir até ela e executar seu código, isso leva uma certa fração de tempo para acontecer o que deixa o programa com uma resposta um pouco menor. Já as funções inline quando são chamadas o código já está lá, porque o compilador trata de copiar todo o código da função para o local onde ela está sendo chamada a partir do momento em que o código é compilado. Ou seja, se criarmos um código contendo uma função inline parecido com o abaixo:

```
void mensagem (){
cout <<"Mensagem que irá aparecer na tela";
}

int main (void){
mensagem ();
}

Quando o compilador compilar este código, ele se tornará apenas:

int main (void){
cout <<"Mensagem que irá aparecer na tela";
}
```

Como se não existisse a função, mas todo seu código é copiado para a posição em que é chamado. Dessa forma o programa não terá que se deslocar até achar a função porque todo seu código já está escrito logo abaixo fazendo com que o tempo de resposta seja maior.

Para criar uma função inline basta fazer a mesma coisa fariamos para criar uma função normal, a única diferença e que antes de começarmos escrever a função deveremos utilizar a palavra reservada inline.

Mas o aumento de desempenho vem com um certo custo de espaço em memória. Queremos dizer que além de aumentar o desempenho, também aumenta o tamanho do arquivo. Por isso, funções inline não são tão utilizadas, ainda mais hoje em dia com computadores extremamente rápidos que conseguem chamar uma função em pouquíssimos milésimos de segundo.

Outra coisa importante a saber é que se colocarmos uma função inline de, por exemplo, 100 linhas de código dentro de uma iteração (repetição, loop) de 50 vezes, o próprio compilador não compilará este código, pois ele entende que será gerado um arquivo exageradamente grande com um custo de recursos do sistema desnecessário.

link: http://www.cplusplus.com/articles/2LywvCM9/


Why to use –
In many places we create the functions for small work/functionality which contain simple and less number of executable instruction. Imagine their calling overhead each time they are being called by callers.
When a normal function call instruction is encountered, the program stores the memory address of the instructions immediately following the function call statement, loads the function being called into the memory, copies argument values, jumps to the memory location of the called function, executes the function codes, stores the return value of the function, and then jumps back to the address of the instruction that was saved just before executing the called function. Too much run time overhead.
The C++ inline function provides an alternative. With inline keyword, the compiler replaces the function call statement with the function code itself (process called expansion) and then compiles the entire code. Thus, with inline functions, the compiler does not have to jump to another location to execute the function, and then jump back as the code of the called function is already available to the calling program.
With below pros, cons and performance analysis, you will be able to understand the “why” for inline keyword
Pros :- 
1.	It speeds up your program by avoiding function calling overhead.
2.	It save overhead of variables push/pop on the stack, when function calling happens.
3.	It save overhead of return call from a function.
4.	It increases locality of reference by utilizing instruction cache.
5.	By marking it as inline, you can put a function definition in a header file (i.e. it can be included in multiple compilation unit, without the linker complaining)

Cons :-
1.	It increases the executable size due to code expansion. 
2.	C++ inlining is resolved at compile time. Which means if you change the code of the inlined function, you would need to recompile all the code using it to make sure it will be updated
3.	When used in a header, it makes your header file larger with information which users don’t care.
4.	As mentioned above it increases the executable size, which may cause thrashing in memory. More number of page fault bringing down your program performance.
5.	Sometimes not useful for example in embedded system where large executable size is not preferred at all due to memory constraints.

When to use - 
Function can be made as inline as per programmer need. Some useful recommendation are mentioned below-
1. Use inline function when performance is needed.
2. Use inline function over macros.
3. Prefer to use inline keyword outside the class with the function definition to hide implementation details.

Key Points - 
1.	It’s just a suggestion not compulsion. Compiler may or may not inline the functions you marked as inline. It may also decide to inline functions not marked as inline at compilation or linking time.
2.	Inline works like a copy/paste controlled by the compiler, which is quite different from a pre-processor macro: The macro will be forcibly inlined, will pollute all the namespaces and code, won't be easy to debug.
3.	All the member function declared and defined within class are Inline by default. So no need to define explicitly.
4.	Virtual methods are not supposed to be inlinable. Still, sometimes, when the compiler can know for sure the type of the object (i.e. the object was declared and constructed inside the same function body), even a virtual function will be inlined because the compiler knows exactly the type of the object.
5.	Template methods/functions are not always inlined (their presence in an header will not make them automatically inline).
6.	Most of the compiler would do in-lining for recursive functions but some compiler provides #pragmas- 
microsoft c++ compiler - inline_recursion(on) and once can also control its limit with inline_depth.
In gcc, you can also pass this in from the command-line with --max-inline-insns-recursive