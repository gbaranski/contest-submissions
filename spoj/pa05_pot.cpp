#include <stdio.h>

int pow(int a, int b) {
  if (b <= 1) return a;
  return a * pow(a, b - 1);
}

int main() {
  char n;
  scanf("%c", &n);
  for(int i = 0; i < n; i++) {
    int a, b;
    scanf("%i", &a);
    scanf("%i", &b);

    printf("%i\n", pow(a, b) % 10);
  }

  return 0;
}
