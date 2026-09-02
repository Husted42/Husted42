#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include "bits.h"

int main() {
  struct bit result = int_to_bool(1);
  printf(result.v?"true\n":"false\n");
  return 0;
}
