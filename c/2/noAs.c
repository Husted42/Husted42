#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include "bits.h"

int main(int argc, char *argv[]) {
    (void)argc; // Indicates that argc is not used

        if (argv[1] != NULL) {
            if (argv[1][0] == 'A' || argv[1][0] == 'a') {
                printf("yes, %s does start with %c!\n", argv[1], argv[1][0]);
            } else {
                printf("No, %s starts with %c!\n", argv[1], argv[1][0]);
            }
        } else {
            printf("No arguments provided.\n");
        }
  return 0;
}

