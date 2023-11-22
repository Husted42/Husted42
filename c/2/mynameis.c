#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int print_arguments(int arg_count, char *arg_list[]) {
    // Print arguements
    for (int i = 0; i < arg_count; ++i) {
            printf("(%d) %s ", i, arg_list[i]);
        } printf("\n");
    return 0;
}

int main(int argc, char *argv[]) {
    //Check the number of given arguemnts argc[0] = filename 
    if (argc == 2) {
        printf("You entered: %s\nYou entered: %s\n", argv[1], argv[1]);
    } else {
        printf("Wrong number of arguments: 2 \n");
        print_arguments(argc, argv);
    }
    return 0;
}