## Vetores e Matrizes

Vetores e matrizes são variáveis compostas homogêneas, ou seja, são agrupamentos de dados que individualmente ocupam o mesmo tamanho na memória e são referenciados pelo mesmo nome, geralmente são individualizadas usando-se índices.

lembre-se, passe o tamanho do array nas funções

Aspas duplas e SImples e o \\0
=> o '\0' representa o caracter nullo. ELe é representado em boleano como false/0 e qualquer outro caracter é representado como true/1. POr conta disso é muito útil para o programa saber se chegou ounão ao fim de aqruivo.

char nome[] = {'r', 'a', 'f', 'a', 'e', 'l', '\0'};
char nome[] = 

```
#include <iostream>
using namespace std;

int main(){
  char nome[] = {'r', 'a', 'f', 'a', 'e', 'l', '\0'};
  int i = 0;

  // 
  while(nome[i]){
    cout << nome[i];
    i++;
  }

}

```

COnselho para loop sobre while: Como o i++ é executado apos ler a linha, podemos tranformar o while anterior no seguinte

```
while(nome[i]){
  cout << nome[i++]
}
```

o i++ sera executado depois de imprimier, como queremos que o seja

Se vocÊ usar aspas duplas, ja vai por esse \0,

```
#include <iostream>
 
using namespace std;
 
float mediaValoresVetor(int vet[], int tam) {
    float soma = 0;
    for (int i = 0; i < tam; i++) {
        soma += vet[i];
    }
    return soma / tam;
}
 
int main()
{
    int vet[] = {1, 2, 3, 4, 5}, acima = 0, tam = 5;
    float media;
    media = mediaValoresVetor(vet, tam);
    cout << "Media: " << media << endl;
 
    for (int i = 0; i < tam; i++) {
        if (vet[i] > media) {
            acima++;
        }
    }
    cout << "Valores acima da media: " << acima << endl;
    cout << "Valores abaixo da media: " << tam - acima;
 
    return 0;
}
```