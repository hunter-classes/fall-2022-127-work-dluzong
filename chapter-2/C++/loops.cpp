#include <iostream>
int main()
{
i = 0;
while (i<10){
  std::cout << i << ",";
  i = i+1;
}
std::cout << std::endl;

auto some_number == 22.3;
std::string s = "hello";
for (auto letter : s){
  std::cout << letter << '-';
}
std::cout << "\n";

char go_again = 'y';
while (go_again == 'y'){
  std::cout << "Continue?";
  std::cin >> go_again;
}

for (i=0;i<10;++i){
  std::cout << x << ",";
}  
std::cout << std:: endl;
  
return 0;
}

//Some notes:
//while loops have 3 parts to them
//1. initialization: setting up the variables you'll be looping
//2. condition: should we continue or exit?
//3. brackets that contain modifier to make sure we exit the loop