#include <iostream>
using namespace std;

int main(int argc, char *argv[]){
  cout << "Quantidade de arqumentos: argc: " << endl;
  // O primeiro argumento é sempre o nome do proprio programra
  // argc: quantidade de arqgumetnos, no minimo 1
  // argv: vetor d epnoreios, uma matriz, ou seja , ponteirode ponteiros
  std::cout << "argv[0]: " << argv[0] << std::endl;
  // argumentos passados
  for(int i = 0; i < argc; i++){
    cout << argv[i] << endl;
  }

  return 0;
}