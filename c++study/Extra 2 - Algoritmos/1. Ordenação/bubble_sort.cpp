#include <iostream>

#define MAX 10

using namespace std;

/*
Bubble Sort:
+ Tempo: O(n^2)
+ Link de animação: https://commons.wikimedia.org/wiki/File:Bubble-sort-example-300px.gif
+ A ideia é coparar dois pares de elementos, e mudar suas posiçôes se um for maior que o
  outro até que o primeiro escolhido ache um valor menor
+ ENtao vc faz um loop duplo, faz quase n^2 comparaçoes, alem de fazer trocas a todo momento

*/
void bubble_sort(int *vetor, int size){
	int aux;
	for(int i = size; i >= 0; i--){
		for(int j = 1; j <= i; j++){
			if(vetor[j - 1] > vetor[j]){
				aux = vetor[j - 1];
				vetor[j - 1] = vetor[j];
				vetor[j] = aux;
			}
		}
	}
}

int main(int argc, char const *argv[]){

  int vetor[MAX];
	int i = 0;

	while(true){
		char resp;
		cout << "Digite um valor para a posicao: " << i << endl;
		cin >> vetor[i];
		cout << "Voce deseja continuar? <S> SIM ou <N> NAO: ";
		cin >> resp;
		if(resp != 'S' && resp != 's')
			break;
		cout << endl;
		i++;
	}

	cout << endl << "Exibindo os valores...\n\n";

	for(int j = 0; j <= i; j++){
		cout << "Valor [" << j<< "] = " << vetor[j] << endl;;
	}

  bubble_sort(vetor, i);

  cout << endl << "Exibindo os valores apos ordenacao...\n\n";

  for(int j = 0; j <= i; j++){
		cout << "Valor [" << j<< "] = " << vetor[j] << endl;;
	}

  return 0;
}
