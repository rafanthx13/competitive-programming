https://www.tutorialspoint.com/cplusplus/cpp_numbers.htm

```
#include <iostream>
#include <cmath>
using namespace std;
 
int main () {
   // number definition:
   short  s = 10;
   int    i = -1000;
   long   l = 100000;
   float  f = 230.47;
   double d = 200.374;

   // mathematical operations;
   cout << "sin(d) :" << sin(d) << endl;
   cout << "abs(i)  :" << abs(i) << endl;
   cout << "floor(d) :" << floor(d) << endl;
   cout << "sqrt(f) :" << sqrt(f) << endl;
   cout << "pow( d, 2) :" << pow(d, 2) << endl;
 
   return 0;
}
```

## Funções


link: http://www.cplusplus.com/reference/cmath/

pow
Raise to power (function )

sqrt
Compute square root (function )

ceil
Round up value (function )

floor
Round down value (function )

abs
Compute absolute value (function )

cos
Compute cosine (function )

sin
Compute sine (function )

##

#include <cmath> // ou <math.h>
#include <iostream>
#include <cstdlib>
using namespace std;

````
int main (void){
    double graus, raio, base, expoente, x;
    cout << "Trigonometria\nDigite o numero dos graus -> ";
    cin >> graus;
    cout << "Geometria\nDigite a distancia do raio do circulo -> ";
    cin >> raio;
    cout << "Potenciacao\nDigite a base -> ";
    cin >> base;
    cout << "Digite o expoente -> ";
    cin >> expoente;
    cin.ignore();
    system ("cls");
    x = pow (base, expoente);
    cout << "O seno de "<<graus<<" e "<<sin(graus)<<endl;
    cout << "O co-seno de "<<graus<<" e "<<cos(graus)<<endl;
    cout << "A tangente de "<<graus<<" e "<<tan(graus)<<endl;
    cout << base<<" elevado a "<<expoente<<" e "<<x<<endl;
    cout << "A raiz quadrada de "<<x<<" e "<<sqrt(x)<<endl;
    cout << "O log2 de "<<x<<" e "<<log(x)<<endl;
    cout << "O log10 de "<<x<<" e "<<log10(x)<<endl;
    cout << "O teto de "<<x<<" e "<<ceil(x)<<endl;
    cout << "A parte inteira de "<<x<<" e "<<floor(x)<<endl;
    cout << "Um circulo com "<<raio<<"cm de raio tem: ";
    cout << raio*2*M_PI<<"cm de comprimento e ";
    cout << pow(raio,2)*M_PI<<"cm de area.\n"<<endl;
    system ("pause");
    return EXIT_SUCCESS;
}
````

