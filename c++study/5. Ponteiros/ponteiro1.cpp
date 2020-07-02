#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
  int var; // Declarar variável
  // Ponteiro é definido pelo '*'
  // VocÊ pode colocálo de duas formas
  // Junto ao tipo ou antes do id da variavel
  int* pvar;
  int *pvar_other;
  // Ponteiro deve receber um endereço para o qual possa apontar
  pvar = &var; // o ponteiro aponta para o endereço de var, devem ter o mesm tipo
  // Para mostrar o conteudo desse endereço, usadmo o '*'
  cout << *pvar << endl; // > 10
  // Como aponta para um endereço eu posso mudar o valor qu esta nesse enderço
  // Usando '*' sobre um ponteiro, eu acesso seu valor
  // Assim, a patir de pvar1, posso mudar a variavel var
  *pvar = 20;
  std::cout << "var" << std::endl; // > 20
  return 0;
}
