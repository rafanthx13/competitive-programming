#include <iostream>
using namespace std;
 
// function declaration
int m(int num1, int num2);
 
int main () {
   // local variable declaration:
   int a = 100;
   int b = 200;
   int ret;
 
   // calling a function to get max value.
   ret = m(a, b);
   cout << "Max value is : " << ret << endl;
 
   return 0;
}
 
// function returning the max between two numbers
int m(int num1, int num2) {
   // local variable declaration
   int result;
 
   if (num1 > num2)
      result = num1;
   else
      result = num2;
 
   return result; 
}