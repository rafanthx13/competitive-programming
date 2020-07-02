/*
  Implementar fila de prioridade com classe
*/

#include <iostream>
#include <queue>
using namespace std;

class Pessoa{

  private:
    string nome;
    int idade;

  public:
    Pessoa(string nome, int idade){
      this->nome = nome;
      this->idade = idade;
    }

    string getNome(){
      return nome;
    }

    int getIdade(){
      return idade;
    }

};

// Usamos essa struct para poder ordenar apartir de elemtnos internos da classe
struct CompIdade{
	bool operator()(Pessoa& p1, Pessoa& p2){
		return p1.getIdade() < p2.getIdade();
	}
};

int main(int argc, char *argv[]){

	priority_queue<Pessoa, vector<Pessoa>, CompIdade> pq;

	Pessoa p1("Joao", 40), p2("Maria", 55), p3("Pedro", 60);
	
	pq.push(p1);
	pq.push(p2);
	pq.push(p3);
	
	Pessoa pessoa = pq.top();
	
	cout << "Nome: " << pessoa.getNome() << endl;
	cout << "Idade: " << pessoa.getIdade() << endl;
	
	return 0;
}