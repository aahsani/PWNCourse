// gcc -fstack-protector-all main.c
// 0xf8bb9500
#include<stdio.h>
#define SIZE 4

int main()
{
    char s[SIZE];
    scanf("%s", s);
    return 0;
}