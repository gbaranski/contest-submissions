#include <bits/stdc++.h>
#include <algorithm>
#include <string>

using namespace std;

typedef long long int lli;

bool isPalindrone(string str) {
  string reversedStr = str;
  reverse(reversedStr.begin(), reversedStr.end());
  return str.compare(reversedStr) == 0;
}


void iterateString(string &str, int index) {
  if(str[index] == '9') {
    str[index] -= 9; // 0
    iterateString(str, index - 1);
  } else {
    str[index]++;
  }
}

void solve() {
  string num;
  cin >> num;

  while(!isPalindrone(num)) {
    iterateString(num, num.size() - 1);
  }

  cout << num;
  cout << "\n";
}

int main() {
  int n;
  cin >> n;
  for(int i = 0; i < n; i++) solve();
}
