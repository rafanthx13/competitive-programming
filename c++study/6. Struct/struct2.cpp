#include <iostream>
using namespace std;

struct Pessoa{
  
  int idade;
  // tornando privado
  // private : int idade;
  int num_sort;

  // metodo constutor
  Pessoa(int idade){
    this->idade = idade;
  }

  Pessoa(int idade, int num_sort){
    this->idade = idade;
    this->num_sort = num_sort;
  }
  
  void setIdade(int idade){
    this->idade = idade;
  }

  int getIdade(){
    return this->idade; // porediar ser so return idade
  }

};

int main(int argc, char const *argv[])
{
  Pessoa pessoa(20); // criar objeto
  // pessoa.idade = 20;
  cout << pessoa.getIdade() << endl;
  return 0;
}
