
void addrPrint(char *pp){
  printf("*pp: %p\n",*pp);
  printf("pp: %p\n", pp);
}

void main(void)
{
  char local_48 [8];
  char auStack64 [24];
  char *local_28;
  char auStack32 [24];

  printf("%p\n", local_48);
  printf("%p\n", auStack64);
  printf("%p\n", local_28);
  printf("%p\n", auStack32);
  printf("--------------------------------\n");
  printf("%p\n", &local_48);
  printf("%p\n", &auStack64);
  printf("%p\n", &local_28);
  printf("%p\n", &auStack32);
  printf("--------------------------------\n");

  addrPrint(&local_28);
  return;
}

