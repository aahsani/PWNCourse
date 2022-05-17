#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void printresult(int r) {
    char number[12];
    puts("\n===================================================================");
    puts("\nThank you for using our system.\nIf you don't mind, leave your phone number for us in order to inform you about our new productions later!");
    puts("\nEnter your phone number: ");
    fgets(number, 0x20, stdin);
    puts("\nThis is the comparison result: ");
    if(r == 0)
        printf("--->   *str1 and str2 are equal*\n");
    else
        printf("--->   *str1 and str2 are not equal*\n");
}

void readline(char* dest, size_t len) {
    char* buf = NULL;
    size_t l;
    getline(&buf, &l, stdin);
    strncpy(dest, buf, len);
}

void compare() {
    char str1[15];
    char canary[12] = "noshellcode\0";
    char str2[15];

    puts("Enter first string (Up to 15 chars): ");
    readline(str1, 15);
    puts("Enter second string (Up to 15 chars): ");
    readline(str2, 25);
    puts("\n\n***Note that we have a canary between these two strings and you can not write any shellcodes!");
    printf("Do not you believe? Here is the canary address:  %p\n", canary);

    int res = strcmp(str1, str2);
    if(strcmp(canary, "noshellcode") == 0)
        printresult(res);
    else{
        printf("\nYou overwrote the canary :|\nNo results for you. Bye Bye.\n");
        printf("%s", canary); 
        printf("--------------------------");
    }
}

void tmulogo(){
    printf("============================================================================\n");
    printf("=       ____  __  __  __  __  ___  ____  ____    ___   ___  ___   __       =\n");
    printf("=      (_  _)(  \\/  )(  )(  )/ __)(_  _)( ___)  (__ \\ / _ \\(__ \\ /  )      =\n");
    printf("=        )(   )    (  )(__)(( (__   )(   )__)    / _/( (_) )/ _/  )(       =\n");
    printf("=       (__) (_/\\/\\_)(______)\\___) (__) (__)    (____)\\___/(____)(__)      =\n");
    printf("=                                                                          =\n");
    printf("============================================================================\n");
}




int main() {
    setbuf(stdout, NULL);
    setbuf(stdin, NULL);
    tmulogo();
    puts("Welcome to the String Comparison System!\nEnter two strings to be compared with each other. \nWe will tell you the comparison result.\n");
    compare();
    return 0;
}
