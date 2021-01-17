#include <stdio.h>

bool isPrime(int num) {
  if (num == 0 || num == 1) return false;

  for(int i = 2; i < num; i++) {
    if (num % i == 0) return false;
  }

  return true;
}


int main() {
  int n;
  scanf("%i", &n);

  for (int i = 0; i < n; i++) {
    int num;
    scanf("%i", &num);
    printf("%s\n", isPrime(num) ? "TAK" : "NIE");
  }

  return 0;
}
