/// Outro exemplo de uso de ponteiros

#include <iostream>
#include <string.h>

using namespace std;

// IMprime a string invertida
int main(int argc, char *argv[])
{
	char nome[100];
	int tam;
	char* p;
	char* pini;

	cout << "Digite um nome: ";
	cin >> nome;

	tam = strlen(nome);
	p = &nome[tam - 1];
	pini = &nome[0];

	while(true){
		cout << *p;
		if(p-- == pini)
			break;
	}
	cout << endl;
	return 0;
}
