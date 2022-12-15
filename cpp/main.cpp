//C++ project
#include <iostream>

//your program must show that you understand an if statement and a loop. You can modify your program in any way to exhibit this.
//Make sure you’ve implemented at least one function that takes in at least one parameter and returns a value.

//Function - takes in two num and returns the greater num
int greater_num(int a, int b){
  int c;
  std::cout <<"Of the two numbers "<< a <<" and "<< b <<"\n";
  if(a > b){
    c = a;
  }
  else {
    c = b;
  }
  std::cout <<"The greater number is: ";
  return c;
}

//Base - prints "Hello World" string
int main() {
  std::cout <<"Hello World!\n";
  std::cout<<"-------------\n";

  //If statement -
  //tests if a num is even or odd
  int num = 24;
  if(num % 2 == 0){
    std::cout <<num<<" is an even number\n";
  }
  else {
    std::cout <<num<<" is an odd number\n";
  }
  std::cout<<"-------------\n";

  //While loop -
  //loops through values and tests whether the value is even or odd and prints result
  int val = 1;
  while(val < 11){
    if(val % 2 == 0){
      std::cout << val <<" is an even number\n";
    }
    else {
      std::cout << val <<" is an odd number\n";
    }
    val = val + 1;
  }
  std::cout << val <<" is an odd number\n";
  std::cout<<"-------------\n";
  
  //Function test - 
  int a, b;
  a = 45;
  b = 62;
  std::cout <<greater_num(a,b)<<"\n";

  return 0; 
}
