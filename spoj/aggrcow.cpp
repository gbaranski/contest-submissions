#include <iostream>
#include <algorithm>


int main() {
  int tests, stalls, cows;
  
  std::cin >> tests;
  std::cin >> stalls;
  std::cin >> cows;
  
  for(int i = 0; i < tests; i++) {
    int stallsLocations[stalls];

    for(int j = 0; j < stalls; j++) {
      std::cin >> stallsLocations[j];
    }
    std::sort(stallsLocations, stallsLocations + stalls);
    for(int j = 0; j < stalls; j++) {
      std::cout << stallsLocations[j] << "\n";
      
    }

  }

  return 0;
}
