// gcc addresses.c -ldl
#include <stdio.h>
#include <stdlib.h>
#include <dlfcn.h>
 
int main()
{
    int stack;
    int *heap = malloc(sizeof(int));
 
    printf("executable: %p\n", &main);
    printf("stack: %p\n", &stack);
    printf("heap: %p\n", heap);
    printf("system@plt: %p\n", &system);
 
    void *handle = dlopen("libc.so.6", RTLD_NOW | RTLD_GLOBAL);
    printf("libc: %p\n", handle);
    printf("system: %p\n", dlsym(handle, "system"));
 
    free(heap);
    return 0;
}