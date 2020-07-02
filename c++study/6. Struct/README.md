# Struct, Classe e Oirentação a Objeto

## Struct

 FUnciona em C++

```
 typedef struct pessoa
{
	char nome[100];
	int idade;
} t_pessoa;

``` 

COlocamos o typedef para que quando chamarmos nao precisarmos colocar struct denovo, assim. No exemplo anterior sera do tipo t_pessoa.

Sem ele vocÊ tera que se receferia a sstruct com `struct pessoa`

```
int main(int argc, char *argv[]){
	t_pessoa pessoas[100]; // vetor de 100 pessoas, vai aloca 00*sizeof(struct pessoa)
	t_pessoa* p;

	p = &pessoas[0];

  // Acessar valor da estrutura
	pessoas[0].idade = 10;
	pessoas[1].idade = 11;
	pessoas[2].idade = 12;

  // se for um ponteiro que esta apontando para sua estruturas, enntao tem que usar `->`
	cout << p->idade << endl;
	cout << (p + 1)->idade << endl;
	cout << (p + 2)->idade << endl;
	return 0;
}
```

Acesso o atributo da struct com '.' quando for uma variavel, quando for um ponireio, tem que usar `->`]

## comparanrod classes e estrauvt

em C++, diferente de C, a strcut é um tipo primitivo.

em struct podese ter metodos,  a principla diferentça sao os modificadores de acesso, em struct, sao smepre publics por default