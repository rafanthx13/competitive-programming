## Ponteiros

### 

Ponteiros  sâo variáveis que guardam endereço de memoria. Eles nao armazenam um valor, eles armazenanm endereços de memoória.

Usamos o asterisco para indicar que é um ponteiro
```
int* var1; // ou
int *var2;
```

é necessário colocar o tipo nos pontteiros pois os tipode tem taamnahosdiferenets

### Operadores

`&`: Endereço
+ Se tenho uma variável comun, o `&` pega seu endereço
`*`
+ Se eu tenho um pontnterio, usar  `*` faz mostrar o valor desse endeço
Se eu tenho
```
int a = 20
int* b = NULL;
```
Perceba que o asterisco `*` é usado na declaraçao pra dizer que uma variável é ponteiro, e usadmo o asterisco denovo somente para buscar o valor de onde aponta, mas nao seu conteuco. Lem-res, seu conteudo é um enderçeo de memoria assim podemos executar ose seguintes trechos de código que estao corretos.

Pgando o enderçeo de a:
```
b = &a;
```
 O POnteiro brecebe o enderço de a &a (&)

 ```
cout << *b
 ```

IMprime o valor do endereço de b, como b tem o enderçeo de a, mostra o valor de a (*)

## Vetores e Array

O vetor que criamos na verdade é um ponteiro, asism, se vocÊ quiser pasasr um vetor por referencia, ocê nao precisa passar com `&` poins um vetor ja aponta para uma posicao de memoria, para o inicio do vetor, e o [0], [1], [2] [3] , ... é pra acessar o valor/endereço da respectiva posicao do vetor.

Tanto é que da mesma forma que manipulamos um vetor podemos manipular um array, o `[]` de um vetor é o meso que o `*` de um ponteiro.

No código abaixo, as duas funçoes acessam da mesma forma o vetor por passagem por referencia

```void funcao_referencia_vetor(int vet[]){
  vet[0] = 70;
}

void funcao_ref_like_ponteiro(int *vet){
  vet[0] = 777;
}

int main(int argc, char const *argv[])
{
  int vetor[10];
  vetor[0] = 7;
  funcao_referencia_vetor(vetor);
  std::cout << "funcao_referencia_vetor :" <<  vetor[0] << std::endl;
  funcao_ref_like_ponteiro(vetor);
  std::cout << "funcao_ref_like_ponteiro: " << vetor[0] <<  std::endl;
  return 0;
}

```

## Funçoes: Passagem por valor  e por referencia.

COmo em C, a passagem no prametro de uma função é por valor e nao por referncia, com isso:

**Nao eh possivel modificar o valor de uma variavel dentrodeu uma função**

Assim, para fazer uma pasagem por referencia deve-se fazer:
1. A funçao tem como parametros ponteiros (exe: (int* arg))
2. QUando vocÊ chamala, voce ve passar um endereço, ou seja, ou aplica um `&` numa variavel ou apenas passe um ponteiro pois ele tem enderçeo de memoria

```
void funcao_passagem_valor(int n){
  n = 20; // nao modifica, pois eh apenas um valor
}

void funcao_passagem_refeerencia(int* n){
  *n = 20; // modifica valor, pois vou mudar o conteudo do endereço
}

int main(int argc, char const *argv[])
{
  int var = 10;
  cout << "varivael var comeca com " << var << endl;
  funcao_passagem_valor(var);
  cout << var << " por valor"  << std::endl;
  funcao_passagem_refeerencia(&var);
  std::cout << var << " por referencia" << std::endl;
  return 0;
}

```


### POnteiros  e constentes
 ```
 #include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
	const int vet[] = {1, 2, 3};
	// const int* || int const* === São a mesma coisa,
	// Ponteiros para valores Constantes
	// => Não é possivel alterar o valor
	// entao nao da pra fazer *p1 = any_value
	const int* p1 = &vet[0];
	int const* p2 = &vet[1];
	// Ponteiro Constante para um Inteiro
	// => Não é possivel alterar o ponteiro
	int* const p3 = new int[3];
	const char* const p4 = "Marcos";

	cout << "*p1 = " << *p1 << endl;
	cout << "*p2 = " << *p2 << endl;

	// EH possivel alterar o valor do ponteiro constante
	*p3 = 1;
	*(p3 + 1) = 2;
	*(p3 + 2) = 3;

	cout << "P3:" << endl;
	cout << *p3 << endl;
	cout << *(p3 + 1) << endl;
	cout << *(p3 + 2) << endl;

	cout << *(p4 + 1) << endl;

	return 0;
}

```