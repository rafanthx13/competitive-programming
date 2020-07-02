#include <iostream>

using namespace std;

void funcao_referencia_vetor(int vet[]){
  vet[0] = 70;
}

void funcao_ref_like_ponteiro(int *vet){
  vet[0] = 777;
  // pode ser acessado tambem como *(vet + 0)
  // ou *(vet + 1) 
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

/* OUTPUT
funcao_referencia_vetor :70
funcao_ref_like_ponteiro: 777

*/
