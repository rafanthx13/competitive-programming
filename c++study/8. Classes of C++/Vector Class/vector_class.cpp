#include <iostream>
#include <vector>

using namespace std;

class Ponto{
public:
	int x, y;

	Ponto(int x, int y){
		this->x = x;
		this->y = y;
	}
};

int main(int argc, char *argv[])
{
	vector<Ponto*> vet;
	vector<Ponto*>::iterator it;
	Ponto* p1 = new Ponto(1, 2);
	Ponto* p2 = new Ponto(3, 4);

  // euivalente ao append de py
	vet.push_back(p1);
	vet.push_back(p2);


  // it é um interrador: assim voce^pode percorred como um 'for each'
  // it é um ponteiro, para acessar seus dados, tem que usar *

  // o v.end() nao retorna o ulo, para acessar o ultimo, tem que ser .end()---
	for(it = vet.begin(); it != vet.end(); it++)
		cout << "(" << (*it)->x << ", " << (*it)->y << ")\n";

	return 0;
}