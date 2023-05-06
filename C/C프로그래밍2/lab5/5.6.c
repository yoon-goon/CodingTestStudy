#include <stdio.h>

int main(int argc, char *argv[]) { // echo 구현
  int i;
  for (i = 1; i < argc; i++)
    printf("%s%s", argv[i], (i < argc-1) ? " " : "");
  printf("\n");
  return 0;
}