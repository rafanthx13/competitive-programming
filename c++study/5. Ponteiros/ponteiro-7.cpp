//ponteiros com constatens

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
