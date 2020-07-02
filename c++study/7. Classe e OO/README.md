# Clases e OO

## COncenitos diferentes do habitual (JAVA)

+ friend fucntion: funão que tem acesso a coisas internas protected de uma classe
+ construtor de copia: por default, o c++ passa um objeto por valor
+ henraça multipla sem interfacae
+ virtual funcionta: para garantir o polimofrismo correnot no c++ como ocore em java
+ classe template: ser acapaz de receber qualquer coisa como python

https://www.javatpoint.com/cpp-virtual-function

Exemplo de classe com atributos e métodos. Bem semelhante a JAVA

```
#include <iostream>

using namespace std;

class Conta{

public:
	int numero;
	double saldo;

	double depositar(double quantidade)	{
		if(quantidade > 0)
			saldo += quantidade;
		return saldo;
	}

	double retirar(double quantidade){
		if(quantidade > 0 && saldo >= quantidade)
			saldo -= quantidade;
		return saldo;
	}
  
};

int main(int argc, char *argv[]){
	Conta c;
	c.numero = 1;
	c.saldo = 100.75;

	cout << "Saldo: " << c.saldo << endl;
	cout << "Saldo depois do deposito: " << c.depositar(100) << endl;
	cout << "Saldo depois do saque: " << c.retirar(-50) << endl;

	return 0;
}

```

## FOrmas de inicializar

1. A comun, atribuido elemetno por elemento

```
Conta c;
	c.numero = 1;
	c.saldo = 100.75;
```

2. Com cahves, atribui valores em ordem de acordo com os atributos da classe

```
Conta c = {1, 100.75}
```

3. Uma forma com ponteiros (para treinar seu uso)

```
Conta c;
Conta* p_c = &c;
(*pc).numero = 1;
(*pc).saldo = 00;
```

4. Outra forma usando ponteiros

```
Conta* novaConta(int numero)
{
	Conta* c = new Conta;
	c->numero = numero;
	c->saldo = 0.0;
	return c;
}

int main(int argc, char *argv[])
{
	Conta* pc = novaConta(1111);

	cout << "Numero: " << pc->getNumero() << endl;
	cout << "Saldo: " << pc->getSaldo() << endl;
	return 0;
}
```



##Escopo de  metodos

EM C++ o ":" é um operador de escopo. Por causa disos, pdemos definir funçoes de uma clase fora dela. Para isso basta atribuot a funçâo ao escopo da classe. E na classe deixo apenas a declaração

```
#include <iostream>

using namespace std;

class Box {
   public:
      double length;         // Length of a box
      double breadth;        // Breadth of a box
      double height;

      // Member functions declaration
      double getVolume(void);
      void setLength( double len );
    
};

// Member functions definitions

double Box::getVolume(void) {
   return length * breadth * height;
}

void Box::setLength( double len ) {
   length = len;

```
## Acesso a metodos e atributos

A class can have multiple public, protected, or private labeled sections. Each section remains in effect until either another section label or the closing right brace of the class body is seen. The default access for members and classes is **private**.

```
class Base { 
   public:
      // public members go here
      protected:
 
   // protected members go here
   private:
   // private members go here
 
};
```
###### public

A public member is accessible from anywhere outside the class but within a program. You can set and get the value of public variables without any member function as shown in the following example.

Public: All the class members declared under public will be available to everyone. The data members and member functions declared public can be accessed by other classes too. The public members of a class can be accessed from anywhere in the program using the direct member access operator (.) with the object of that class.

###### private

A private member variable or function cannot be accessed, or even viewed from outside the class. Only the class and friend functions can access private members.

Practically, we define data in private section and related functions in public section so that they can be called from outside of the class as shown in the following program.



Private: The class members declared as private can be accessed only by the functions inside the class. They are not allowed to be accessed directly by any object or function outside the class. Only the member functions or the friend functions are allowed to access the private data members of a class.

###### protected

A protected member variable or function is very similar to a private member but it provided one additional benefit that they can be accessed in child classes which are called derived classes.

Protected: Protected access modifier is similar to that of private access modifiers, the difference is that the class member declared as Protected are inaccessible outside the class but they can be accessed by any subclass(derived class) of that class.

A diferença para o privado é como ele haje comherança

###### Como usar:
private: para as variaveis
public: para os metodos em geral  aserem utilizados. É o que vocÊ expoe para ser usado fora da classe
protected: para metodos internos da classe, como um auxiliar dos métodos publics


## friend functions

+ Ao fazer isso, uma funçâo pode usar um método  de uma classe.
+ Exemplo: VOcê viaja e nao quer deixar usa casa exposta, mas quer que alguem va la olhar ela

https://www.geeksforgeeks.org/friend-class-function-cpp/

Friend Class A friend class can access private and protected members of other class in which it is declared as friend. It is sometimes useful to allow a particular class to access private members of other class. For example a LinkedList class may be allowed to access private members of Node.

```
class Box {
   double width;
   
   public:
      friend void printWidth( Box box );
      void setWidth( double wid );
};

// Member function definition
void Box::setWidth( double wid ) {
   width = wid;
}

// Note: printWidth() is not a member function of any class.
void printWidth( Box box ) {
   /* Because printWidth() is a friend of Box, it can
   directly access any member of this class */
   cout << "Width of box : " << box.width <<endl;
}
```

Nesse exemplo acima, printWidth é uma friend fucntion, declarada fora da classe. Mas, comotem sua acintarua dentro dela, ela pode acessar métodos e atributos da classe no seu escopo.

## COnstrutores e Destrutores

COnstrutrot

EM geral nao tem argumento. Ele nao retorna nada e tem que ser public

Destrutor

É o nome da classe com um tio  `~`. Sme tipo de retorno. ELe é usado de forma automatica de acordo com o escopo de acordo com a execução do programa. É mais um especificaçâo de como e o que fazer ao deletealo

A destructor is a special member function of a class that is executed whenever an object of it's class goes out of scope or whenever the delete expression is applied to a pointer to the object of that class.

A destructor will have exact same name as the class prefixed with a tilde (~) and it can neither return a value nor can it take any parameters. Destructor can be very useful for releasing resources before coming out of the program like closing files, releasing memories etc.

Following example explains the concept of destructor −

```

#include <iostream>
#include <string.h>

using namespace std;

class Pessoa
{
private:
	char nome[100];
	int idade;
	int* parentes;
public:
	Pessoa(const char* nome, int idade)
	{
		strcpy(this->nome, nome);
		this->idade = idade;
		parentes = new int[100];
		cout << "Entrou no construtor: " << nome << endl;
	}
	char * getNome()
	{
		return nome;
	}
	int getIdade()
	{
		return idade;
	}
	~Pessoa()
	{
		cout << "Entrou no destrutor: " << nome << endl;
		delete[] parentes;
	}
};

int main(int argc, char *argv[])
{
	Pessoa pessoas[3] =
	{
		{"joao", 30}, {"maria", 20}, {"pedro", 40},
	};

	//cout << "Nome: " << p.getNome() << endl;
	//cout << "Idade: " << p.getIdade() << endl;
	return 0;
}
// contrutor e destrutor sao cahamdaos 3 vezes
// o destrutor e chamdao pois encontrou o return 0
```

## SObrecarga

### SObrecarga de construtor


```
#include <iostream>

using namespace std;

class Carro
{
public:
	int ano;
	double preco;

	Carro()
	{
		ano = 0;
		preco = 0.0;
	}
	Carro(int ano)
	{
		this->ano = ano;
		this->preco = 0.0;
	}
	Carro(int ano, double preco) {
		this->ano = ano;
		this->preco = preco;
	}
};

int main(int argc, char *argv[])
{
	Carro carro;
	Carro carro2(2014);
	Carro carro3(2014, 200000);

	cout << "Preco do carro: " << carro.preco << endl;
	cout << "Preco do carro2: " << carro2.preco << endl;
	cout << "Preco do carro3: " << carro3.preco << endl;
	return 0;
}
```

## Contrutor de copia

A copia funciona semelhante ao python. Se for algo simples deuma unica camada, o c++ passa a copia dos valores para funôes e para copiar. Esta é a copia superficial, e dependendo dos seus dados srá necessária criar um construtor de copias pois essa copia surpeficaial é apenas de um primeiro nivel de variaveis.. Agora, se for, uma struct, com um vetor com um vetor com uma strcut ou algo do tipo, é necessáriao fazer uma cópia profunda.

Crei se seua classe for complexa e precisa passar ela apra um paramteros. Sem fazre um copy contructor correot, vvai dar problema pois a copia superfciaial vai apresentar daodsd invaldios


The copy constructor is a constructor which creates an object by initializing it with an object of the same class, which has been created previously. The copy constructor is used to −

Initialize one object from another of the same type.
Copy an object to pass it as an argument to a function.
Copy an object to return it from a function.
If a copy constructor is not defined in a class, the compiler itself defines one.If the class has pointer variables and has some dynamic memory allocations, then it is a must to have a copy constructor. The most common form of copy constructor is shown here −

Sintaxe
```
classname (const classname &obj) {
   // body of constructor
}
```

```
#include <iostream>
#include <string.h>

using namespace std;

class Estudante
{
protected:
	char* nome;

public:
	Estudante(const char* nome)
	{
		cout << "Construindo objeto: " << nome << endl;
		int tam = strlen(nome) + 1;
		this->nome = new char[tam];
		strcpy(this->nome, nome);
	}

	Estudante(const Estudante& e)
	{
		cout << "Construindo copia de " << e.nome << endl;

		int tam = strlen(e.nome) + strlen("Copia de ") + 1;
		this->nome = new char[tam];
		strcpy(this->nome, "Copia de ");
		strcat(this->nome, e.nome);
	}

	~Estudante()
	{
		cout << "Destruindo... " << nome << endl;
		delete[] nome;
		nome = 0;
	}

	const char* getNome()
	{
		return nome;
	}
};

void foo2(Estudante e)
{

}

void foo()
{
	Estudante estudante("joao");
	foo2(estudante); // foo3 vai chamar o contrutor de copia, que especificamos
	cout << "Estudante " << estudante.getNome() << endl;
}

int main(int argc, char *argv[])
{
	foo();

	return 0;
}
```

## Herança

#### classe base (pai) e dereivada (filha)

A class can be derived from more than one classes, which means it can inherit data and functions from multiple base classes. To define a derived class, we use a class derivation list to specify the base class(es). A class derivation list names one or more base classes and has the form −

class derived-class: access-specifier base-class
Where access-specifier is one of public, protected, or private, and base-class is the name of a previously defined class. If the access-specifier is not used, then it is private by default.

Exemplo

```
#include <iostream>
#include <string.h>

using namespace std;

class Animal
{
protected:
	char* nome;

public:
	Animal(const char* nome)
	{
		cout << "Construindo animal..." << endl;
		this->nome = new char[strlen(nome) + 1];
		strcpy(this->nome, nome);
	}
	~Animal()
	{
		delete[] nome;
		nome = 0;
	}
	const char* getNome()
	{
		return nome;
	}
};

class Cachorro : public Animal
{
protected:
	int idade;

public:
	Cachorro(const char* nome): Animal(nome)
	{
		cout << "Construindo cachorro..." << endl;
		idade = 0;
	}
	int getIdade()
	{
		return idade;
	}
	void setIdade(int idade)
	{
		this->idade = idade;
	}
};

int main(int argc, char *argv[])
{
	Cachorro c("yankee");
	c.setIdade(5);

	cout << "Nome: " << c.getNome() << endl;
	cout << "Idade: " << c.getIdade();
	return 0;
}
```



#### Access Control and Inheritance
A derived class can access all the non-private members of its base class. Thus base-class members that should not be accessible to the member functions of derived classes should be declared private in the base class.

We can summarize the different access types according to - who can access them in the following way −

Access	public	protected	private
Same class	yes	yes	yes
Derived classes	yes	yes	no
Outside classes	yes	no	no
A derived class inherits all base class methods with the following exceptions −

Constructors, destructors and copy constructors of the base class.
Overloaded operators of the base class.
The friend functions of the base class.


#### Type of Inheritance
When deriving a class from a base class, the base class may be inherited through public, protected or private inheritance. The type of inheritance is specified by the access-specifier as explained above.

We hardly use protected or private inheritance, but public inheritance is commonly used. While using different type of inheritance, following rules are applied −

Public Inheritance − When deriving a class from a public base class, public members of the base class become public members of the derived class and protected members of the base class become protected members of the derived class. A base class's private members are never accessible directly from a derived class, but can be accessed through calls to the public and protected members of the base class.

Protected Inheritance − When deriving from a protected base class, public and protected members of the base class become protected members of the derived class.

Private Inheritance − When deriving from a private base class, public and protected members of the base class become private members of the derived class.

#### Multiple Inheritance
A C++ class can inherit members from more than one class and here is the extended syntax −

```
class derived-class: access baseA, access baseB....
```

class derived-class: access baseA, access baseB....
Where access is one of public, protected, or private and would be given for every base class and they will be separated by comma as shown above.

```
#include <iostream>
 
using namespace std;

// Base class Shape
class Shape {
   public:
      void setWidth(int w) {
         width = w;
      }
      void setHeight(int h) {
         height = h;
      }
      
   protected:
      int width;
      int height;
};

// Base class PaintCost
class PaintCost {
   public:
      int getCost(int area) {
         return area * 70;
      }
};

// Derived class
class Rectangle: public Shape, public PaintCost {
   public:
      int getArea() {
         return (width * height); 
      }
};

int main(void) {
   Rectangle Rect;
   int area;
 
   Rect.setWidth(5);
   Rect.setHeight(7);

   area = Rect.getArea();
   
   // Print the area of the object.
   cout << "Total area: " << Rect.getArea() << endl;

   // Print the total cost of painting
   cout << "Total paint cost: $" << Rect.getCost(area) << endl;

   return 0;
}
```

## Polimofismo 

### VIrtual FUnctions

+ A C++ virtual function is a member function in the base class that you redefine in a derived class. It is declared using the virtual keyword.
+ It is used to tell the compiler to perform dynamic linkage or late binding on the function.
+ There is a necessity to use the single pointer to refer to all the objects of the different classes. So, we create the pointer to the base class that refers to all the derived objects. But, when base class pointer contains the address of the derived class object, always executes the base class function. This issue can only be resolved by using the 'virtual' function.
A 'virtual' is a keyword preceding the normal declaration of a function.
+ When the function is made virtual, C++ determines which function is to be invoked at the runtime based on the type of the object pointed by the base class pointer.
+ Late binding or Dynamic linkage
+ In late binding function call is resolved during runtime. Therefore compiler determines the type of object at runtime, and then binds the function call.

Rules of Virtual Function

+ Virtual functions must be members of some class.
+ Virtual functions cannot be static members.
+ They are accessed through object pointers.
+ They can be a friend of another class.
+ A virtual function must be defined in the base class, even though it is not used.
+ The prototypes of a virtual function of the base class and all the derived classes must be identical. If the two functions with the same name but different prototypes, C++ will consider them as the overloaded functions.
+ We cannot have a virtual constructor, but we can have a virtual destructor
Consider the situation when we don't use the virtual keyword.

#### Por que usar virtual funcitons

https://stackoverflow.com/questions/2391679/why-do-we-need-virtual-functions-in-c

É o seguinte. Difernete do Java que faz polimofrismo pelo tipo, o C++é, digameos, burro e nao faz em todos os casos. Cenario: uma classe fapi com o metodo foo() e uma classe filha tambem com o método foo(). O C++ faz o polimofrismo correto se DEIXARMOS EXPLICITO QUE ESTAMOS EXECUTADNO O MÉTODO DA CLASSE FILHA. Digamos que tenhamos uma função que recebe como parametro a classe pai. A classe filha tambem pode ser passada já que ela é como a pai. Se executarmos o foo() . dentro dese método AÍ VAI DAR PROBLEMA. POis oq ue veio no escopo foi a classe pai, a classe filha tambem é aceita so que ela nao exeuta seu método foo, vai exeutar o seu super, o do pai. Nesse caos, a soluçâo para funcionar da forma que quermos é adicionar 'virtaual' ao método foo() da classe pai

## SObreCarga (Overloading)

COmo em Java é definri uma mesma funçâo com uma assintaura difenrete: com uma quantidade de parametros deiferentes ou tipos difenretes
```#include <iostream>
using namespace std;
 
class printData {
   public:
      void print(int i) {
        cout << "Printing int: " << i << endl;
      }
      void print(double  f) {
        cout << "Printing float: " << f << endl;
      }
      void print(char* c) {
        cout << "Printing character: " << c << endl;
      }
};

int main(void) {
   printData pd;
 
   // Call print to print integer
   pd.print(5);
   
   // Call print to print float
   pd.print(500.263);
   
   // Call print to print character
   pd.print("Hello C++");
 
   return 0;
}

```


## SObrecarga de Operador prmitivo

Os operadores que conhecemos são como +,-,* e /. EM c++ voce pode definri esses operadores para uma classe.

FUncione bem legal para podeer usar operadores com classe

##### quais que podem

+	-	*	/	%	^
&	|	~	!	,	=
<	>	<=	>=	++	--
<<	>>	==	!=	&&	||
+=	-=	/=	%=	^=	&=
|=	*=	<<=	>>=	[]	()
->	->*	new	new []	delete	delete []

####### QUais que nao podem

::	.*	.	?:


```// Sobrecarga do operador +
 
#include <iostream>
 
using namespace std;
 
class Complexo{
public:
	int real, imag;
 
	Complexo(int real, int imag){
		this->real = real;
		this->imag = imag;
	}
 
	Complexo operator+(Complexo& c){
		return Complexo(this->real + c.real, this->imag + c.imag);
	}
};
 
int main(int argc, char *argv[]){
	Complexo c1(1, 2), c2(3, 4);
	Complexo c3 = c1 + c2;
	//Complexo c3 = c1.operator+(c2);
 
	cout << "Parte real: " << c3.real << endl;
	cout << "Parte imaginaria: " << c3.imag << endl;
	return 0;
}
```



```