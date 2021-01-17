#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_CHARACTERS 10

char* solve() {
  char *buf = (char*)malloc(100 * sizeof(char));
  if (buf == NULL) return NULL;
  scanf("%99s", buf);
  if (strlen(buf) < MAX_CHARACTERS) {
    return buf;
  }

  char cstr[3];
  sprintf(cstr, "%lu", strlen(buf) - 2);

  char *res = (char*)malloc(5 * sizeof(char));
  strncat(res, buf, 1);  // add first character
  strncat(res, cstr, 2); // add amount of characters between
  strncat(res, &(buf[strlen(buf) - 1]), 1); // add last character

  return res;
}

int main() {
  int n;
  scanf("%d", &n);
  for(int i = 0; i < n; i++) {
    char* str = solve();
    printf("%s\n", str);
  }
}
