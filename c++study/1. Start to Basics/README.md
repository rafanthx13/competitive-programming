# 1. Study Basics - INtro a C++

## LInks úteis
+ 

## Links de conteudo útil
+ https://pt.wikiversity.org/wiki/Curso_de_C%2B%2B
+ https://pt.cppreference.com/w/cpp
+ http://excript.com/curso-cpp.html
+ https://www.tutorialspoint.com/cplusplus/index.htm
+ LInk de doc das libs: http://www.cplusplus.com/reference/cmath/
+ Microsoft (Muito Bom em BR): https://docs.microsoft.com/pt-br/cpp/cpp/

## Nome C++

link: http://www.tiexpert.net/programacao/c/introducao-cpp.php

O nome C++
Durante sua fase inicial de desenvolvimento, a linguagem era chamada "novo C" ou ainda "C com classes". O termo "C++" é creditado a Rick Mascitti[6], e foi utilizado pela primeira vez em dezembro de 1983. Ele é uma referência ao operador de incremento ++, significando um acréscimo (uma evolução) à linguagem C. Em tom humorado, desenvolvedores software e especialistas em informática no início da década de 1990 costumavam relacionar o ++ do nome à grande insistência dos programadores em utilizar o C++ da mesma forma que a linguagem C, não usufruindo das novas facilidades que a linguagem poderia fornecer. Assim como o ++ estava sendo aplicado de maneira pós-fixa à letra C, a linguagem C++ era uma evolução do C pós-fixada, que só tornar-se-ia realidade em algum futuro remoto, não naquele momento.

## Caracteristicas

links: conferir depois
http://excript.com/cpp/visao-geral-linguagem-cpp.html

+ Case Sensitive: Diferencia maiusculo de minusculo (SQL, por exmeplo, nao é case Sensitive)

## Diferenças entre C e C++

link: http://excript.com/curso-cpp.html

QUAL A DIFERENÇA ENTRE A LINGUAGEM C E A LINGUAGEM C++?
O C++ é uma extensão da linguagem C. Inclusive, o ++ significa incremento e quer dizer que, o C++ é a evolução da Linguagem C. Evolução NÃO É sinônimo de melhor! O C++ é uma linguagem que permite um desenvolvimento melhor estruturado, porém, essa estruturação faz com que o mesmo seja mais lento do que a linguagem C. Até hoje, a linguagem C é amplamente utilizada, bem como o C++ e, há situações em que o C é a melhor opção mas, na maioria das vezes, o C++ é quem será.

A teoria diz que, todo código C é compatível com o código C++ e deve ser compilado sem quaisquer problema ou erro. Então, temos que o C é compatível com o C++, mas o C++ não é compatível com o C. Podemos dizer que todo programa escrito em C, será processado por compiladores C++. Em teoria o conceito é verdadeiro, na prática, é melhor testar para ter certeza!

O que fez da Linguagem C++ uma grande evolução, foi a introdução da Programação Orientada a Objetos, isto é, utilizaram a Linguagem C como base para a construção de uma nova linguagem, que possui a mesma sintaxe, porém, com novas instruções que permitem definir as informações como entidades abstratas de dados que, comumente chamamos de classes, ou então, objetos.

## Arquivos

`.cpp`: arquivo de C++ (c_plus_plus)

- Header files should use a .h__ extension (.h / .hpp / .hxx). Which of those you use doesn't matter.
- C++ Source files should use a .c__ extention (.cpp / .cxx / .cc). Which of those you use doesn't matter.
- C Source files should use .c (.c only).

## Configurando VS Code

+ O VS COde é um editor que possui vários plugins para o C++. Com o `code runner` vocÊ pode executar o programa com  CTRL + ALT+ N

+ Outra alternativa é fazer com  um que compil, cria o compilado e roda, que é: CTRL +SHIFT + P: ABRE O COMAND PALLTE E DEPOIS CLICA F6 PARA EXECUTAR ESSA OPÇÃO

+ CTRL + SPACE: Abre os snipessets que voce pode isntalr

### snipsets uteis no VSCODE
Onde: "|" é onde para o cursor  e entre %% é o proximo campo ao dar um tab
+ `#inc<`: vai cirar `#include <|>
+ `main`: cria a funcao main com seus argumentos e return 0

## Hello World

```
#include <iostream>
using namespace std;

/*
Comentario de multiplas linhas
*/

// fim do programa Hello World!

int main() 
{
    cout << "Hello, World!" << endl;
    return 0;
}

```

Descrição:
+ `#include <iostream>`: Biblioteca padrão de I/O de C++
+ `cout`: O objeto cout representa o stream de saída no C++. Este stream é uma espécie de seqüência (fluxo) de dados a serem impressos na tela. Para realizar a impressão, usa-se o "operador de inserção" que "insere" dados dentro do stream.
+ `using namespace std;`: especifica para usar o namespace std. Assim, o `cout` que é um objeto desse namespace nâo precisarár por com namespace.
 - Outra alternativa é so usar um namspace próprio: `using std::cout;`
 - Ou seja, sem essa linha, teriamos que charmar `cout` e outros métodos do objro `std` como : `std::cout`
 - endl é também um simbolo do 'std', entao, sem o using name, teriamos que usar "std:endl"
+ `main`: como em C, a função principal é a main
+ `endl`: é o simolbo do \n como constante no C++
+ `return 0;` : Como em C, tem que especificar um retorno.


## Compilando e Executando no terminal

### LInux

INstale o hg++
```
> sudo apt-get g++
```

COmpile o arquivo especificando o arquivo de saida.
+ Se você fizer só `g++ hello-world.cpp`vai gerar sempre por default um `a`.

```
g++ -o hello hello-world.cpp
```

Executar: No linux, como é execuátvel, nao precisa de extensao

```
./hello
```

## namesapce

+ Serve para nao repetir nomes.
+ Serve para definir escopo.
Exemplo:
+ Se voce faz: cout < "abc"
 - ele vai procurar no seu código a função cout e nao vai achar
+ Agora se você faz "using namespace std" ou "std:cout" voce esta especificando o namespace, entao vai buscar o da lib

+ Namespaces in C++ are used to organize too many classes so that it can be easy to handle the application.

For accessing the class of a namespace, we need to use namespacename::classname. We can use using keyword so that we don't have to use complete name all the time.

In C++, global namespace is the root namespace. The global::std will always refer to the namespace "std" of C++ Framework.

+ Em geral é para poder usar com biliotecas. Observe o exemplo abaixo. COm namSpace, acessando um name space com `::` eu posso escolher um méotodo e de qualquer biblioteca *SEM HAVER COMFLITO DE NOMES*
```
#include <iostream>  
using namespace std;  
namespace First {    
    void sayHello() {   
        cout<<"Hello First Namespace"<<endl;          
    }    
}    
namespace Second  {    
       void sayHello() {   
           cout<<"Hello Second Namespace"<<endl;   
       }    
}   
int main()  
{  
 First::sayHello();  
 Second::sayHello();  
return 0;  
}  
```

## Erros comuns

Alguns erros comuns que você deve verificar quando ocorrem erros de compilação no seu código:

Esquecer do ponto-e-vírgula no fim das instruções;
Usar uma variável sem ter-lhe atribuído valor inicial;
Tentar utilizar uma variável local fora de seu escopo;
Colocar ponto-e-vírgula após definir uma constante com #define;
Declarar a variável com um tipo de dados e atribuir um valor diferente do tipo. Ex: int numero = 5.5;
Não definir valor inicial para uma constante declarada com #define;
Atribuir um valor para uma variável tipo caracter (char) sem aspas ou com aspas duplas (Ex: "a"). O correto é aspas simples (Ex: 'a');
Utilizar vírgula em números decimais em vez de ponto.

## Declarar variáveis
SIntae: [tipo] [nome] [opcional: [= valor inicial]];
+ Declara várias vezes
```
int idade, Idade, idade2; // crio 3 variavies, (idade != Idadde)
```

+ `int`:

Tipo	Descrição
void	não é associado a nenhum tipo de dado
int	número inteiro
float	número fracionário ("ponto flutuante")
double	número fracionário de precisão dupla
char	caractere (usa aspas simples, um unico char)
Além destes, o C++ define mais dois: 'bool' e 'wchar_t'.

Tipo	Descrição
bool	Valor Booleano: 'true' ou 'false' (verdadeiro ou falso)
wchar_t	caractere wide (?)



Lógico (booleano)
É o tipo mais simples, e pode armazenar apenas dois valores: verdadeiro ou falso. Para definir esses valores você deve proceder ao seguinte:

bool logico1 = true; // True significa verdadeiro em inglês;
bool logico2 = false; // False significa falso em inglês;
bool logico3 = 0; // Atribui-se o inteiro 0 (zero) equivale a 'false';
bool logico4 = 189; // Qualquer valor diferente de 0 (zero) é interpretado como 'true';

### define

#define PI 3.1415

A sintaxe para isso é (nesse caso, não coloque ponto-e-vírgula no final):

#define [nome da constante] [valor]
Você deverá incluir a diretiva de pré-processador #define antes do início do código:

### COnstantes

Devem sempre se inicializadas quando delcardas, quando você nao faz isso, da erro. POir isso seu valor é imutável

const double pi = 3.1415;  // nao precisa ser no inicio do progmrar

Use a palavra reservadda `cont`

Há tambem a junçao de constantes e ponteiros que sera visto na parte de ponteiro



## Operadores
BEST LINK
https://www.tutorialspoint.com/cplusplus/cpp_operators.htm
https://docs.microsoft.com/pt-br/cpp/cpp/cpp-built-in-operators-precedence-and-associativity?

+
-
*
/: lembrando ha duas diviso
%
++ : como em c, o ++ na frente soma no fim da instruçao, o ++ atras ja soma antes de começar a funçao
+=,
-=
*=
/=


OS MESMSO DE C
#### operadores relacionais
OS MESMSO DE C
#### operadores logicos
OS MESMSO DE C

## Operador ternátio
COmo em JS, a depender de uma condiçao, uma variavel recebe um valor ou outro
|variável| = <condição> ? <valor1> : <valor2>;

## pALAVRAS RESERVADAS

asm, auto, break, case, catch, char, class, const, continue, default, delete, do, double, else, enum, extern, float, for, friend, goto, if, inline, int, long, new, operator, private, protected, public, register, return, short, signed, sizeof, static, struct, switch, template, this, throw, try, typedef, union, unsigned, virtual, void, volatile, wchar_t, while.

lINK PARA O QUE É CADA UMA: https://en.cppreference.com/w/cpp/keyword

## Chars especiais
link: https://www.tutorialspoint.com/cplusplus/cpp_constants_literals.htm
Escape sequence	Meaning
\\	\ character
\'	' character
\"	" character
\?	? character
\a	Alert or bell
\b	Backspace
\f	Form feed
\n	Newline
\r	Carriage return
\t	Horizontal tab
\v	Vertical tab
\ooo	Octal number of one to three digits
\xhh . . .	Hexadecimal number of one or more digits




para ver namespace:
https://docs.microsoft.com/pt-br/cpp/cpp/namespaces-cpp?view=vs-2019




COlcoar no primeiro prograrmara


http://www.cplusplus.com/doc/tutorial/program_structure/
http://www.cplusplus.com/doc/tutorial/basic_io/


# IMPORTANT
Leia e retire toda a informaçâo desses links:
https://isocpp.org/wiki/faq/coding-standards
https://isocpp.org/wiki/faq/big-picture
https://isocpp.org/wiki/faq/freestore-mgmt
https://isocpp.org/wiki/faq/c


## Operador Ternário

```
/*
Operador ternário ?:
<condicao> ? <operacao 1> : <operacao 2>;
num > 10 ? cout << "maior" : cout << "menor ou igual";
*/
```

## setw

usado em fluxos, ou seja, pode ser usado no cout (print do c++).

É colocar um dados e por ele de tamanho fixo que voce define e justificalo a direita. (setw(n))

ELe pega um valor e o deixa com um tamanho definido. Bom para imprimir de forma bonita

Exemplo: eu tenho a string Marta

cout << marta //Marta

Agora seu eu colocar co setw(10)

cout << setw

Exemplo:

```
#include <sstream>  
#include <iostream>  
#include <iomanip>  
using namespace std;  
  
int main()  
{  
    cout << "no setw:" << 42 << '\n'  
              << "setw(6):" << setw(6) << 42 << '\n'  
              << "setw(6), several elements: " << 89 << std::setw(6) << 12 << 34 << '\n';  
    istringstream is("hello, world");  
    char arr[10];  
    is >> setw(6) >> arr;  
    cout << "Input from \"" << is.str() << "\" with setw(6) gave \""  
              << arr << "\"\n";  
    return 0;  
}  
```

Saida

```
no setw:42
setw(6):    42
setw(6), several elements: 89    1234
Input from "hello, world" with setw(6) gave "hello"
```

### keyword 'extern'


linkBR: https://forum.imasters.com.br/topic/419413-como-usar-o-extern/

É como uma variável global. VOcê avisa ao compiladro

A VARIAVEL EXTERN É VISÍVEL EM TODO O PROGRMARA E SREVE PARA SER VISIVEL EM OUTROS MOÓDULOS.

Funçôes, pode default já sâo extern, agora, se você importa um codigo '.cpp' voceê tem qu eusar exern para variável, para funçôes nâo.


você usa extern para mostrar em outros arquivos que existe tal variável global, mas que ela foi declarada em outro arquivo.


This comes in useful when you have global variables. You declare the existence of global variables in a header, so that each source file that includes the header knows about it, but you only need to “define” it once in one of your source files.

To clarify, using extern int x; tells the compiler that an object of type int called x exists somewhere. It's not the compilers job to know where it exists, it just needs to know the type and name so it knows how to use it. Once all of the source files have been compiled, the linker will resolve all of the references of x to the one definition that it finds in one of the compiled source files. For it to work, the definition of the x variable needs to have what's called “external linkage”, which basically means that it needs to be declared outside of a function (at what's usually called “the file scope”) and without the static keyword.

## static


 COmo em Java, ao declara ao static, ele nao sai dea memoria, e toda a sua declaraçâo passa a  nao fazer nada caso já for criado. ENfim, é comom em Java
```
#include <iostream>
using namespace std;

int gerarID()
{
	static int ID = 0;
	return ID++;
}

int main(int argc, char *argv[])
{
	string nome;

	while(true)
	{
		cout << "Digite o nome da pessoa: ";
		cin >> nome;
		cout << "ID gerado para o usuario " << nome << ": " << gerarID() << "\n\n";
	}
	return 0;
}
```

## get  getline: pegar corretamente uma string
Para inserir uma string, usadmos o seguinte trecho
`cin >> nome`
'cin'Vai ler do teclado  e colcoar em nome

O problema é que, como em C, ele não pega se tiver espaço em branco

Para pegar toda uma linha, usamos

Se para ler uma string você usar 

```
#include <iostream>
#define MAX 10
using namespace std;

int main(int argc, char *argv[])
{
	char nome[MAX];
	
	cout << "Digite o seu nome: ";
	//cin >> nome;
	cin.get(nome, MAX);
	cout << "Oi " << nome << endl;
	return 0;
}
```

getline (nao sei a difereneça do get)

```
#include <iostream>     // std::cin, std::cout

int main () {
  char name[256], title[256];

  std::cout << "Please, enter your name: ";
  std::cin.getline (name,256);

  std::cout << "Please, enter your favourite movie: ";
  std::cin.getline (title,256);

  std::cout << name << "'s favourite movie is " << title;

  return 0;
}
```