#include <stdio.h>

int factorial(int num) {
  if(num == 0) return 1;
  return num * factorial(num - 1);
}

int main() {
  int n; 
  scanf("%i", &n);

  for (int i = 0; i < n; i++) {
    int num;
    scanf("%i", &num);
    if (num > 9) {
      printf("0 0\n");
    } else {
      num = factorial(num) % 100;
      printf("%i %i\n", num / 10, num % 10);
    }

  }

  return 0;
}
