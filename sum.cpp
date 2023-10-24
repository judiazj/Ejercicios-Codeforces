#include <iostream>
using namespace std;

int main() {
  int a;
  cin >> a;
  for(int i = 0; i < a; i++) {
    int n;
    cin >> n;
    if(n<7 or n == 9){
      cout << "NO\n";
    }else if(n % 3 != 0){
      cout << "YES\n" << n-3<<" "<< 2 << " " << 1 << "\n";
    }else{
      cout << "YES\n"<< n-5 << " "<< 4 << " " << 1 << "\n";
    }
    }
}