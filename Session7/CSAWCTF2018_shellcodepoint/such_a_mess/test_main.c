#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void printresult(int r) {
    char name[12];
    puts("What is your name?");
    fgets(name, 0x20, stdin);
    printf("Thanks %s. This is the comparison result:\n", name);
    if(r == 0)
        printf("str1 and str2 are equal.\n");
    else
        printf("str1 and str2 are not equal.\n");
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
    readline(str1, 27);
    puts("Enter second string (Up to 15 chars): ");
    readline(str2, 15);
    puts("Note that we have a canary between these two strings and you can not write any shellcodes!\n");
    printf("Do not you believe? Here is the canay address:  %p\n", canary);

    int res = strcmp(str1, str2);
    if(strcmp(canary, "noshellcode") == 0)
        printresult(res);
    else
        puts("You overwrote the canary :|\n No results for you. Bye Bye.\n"); 
}

int main() {
    setbuf(stdout, NULL);
    setbuf(stdin, NULL);
    puts("Welcome to the String Comparison System!\n Enter two strings to be compared with each other. \nWe will tell you the comparison result.\n");
    compare();
    return 0;
}
