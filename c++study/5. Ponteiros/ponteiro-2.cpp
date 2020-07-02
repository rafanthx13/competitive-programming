// Funẫo - Passagem dpor valor e por referência
#include <iostream>

using namespace std;

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

/*
varivael var comeca com 10
10 por valor
20 por referencia
*/
