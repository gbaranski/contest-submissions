#include <iostream>
#include <string>

using namespace std;

void solve() {
  string str;
  cin >> str;
  
  // iterate over every char in str
  for(int j = 0; j < str.size(); j++) {
    int foundDupes = 0;
    for (int i = j + 1; i < str.size(); i++) {
      if(str[j] == str[i]) foundDupes++;
      else break;
    }

    if(foundDupes >= 2) {
      cout << str.substr(j, 1);
      cout << foundDupes + 1;
      j += foundDupes;
    } else {
      cout << str.substr(j, 1);
    }
  }
  cout << "\n";
}

int main() {
  int n;
  cin >> n;
  for (int i = 0; i < n; i++) {
    solve(); 
  }
  

  return 0;
}
