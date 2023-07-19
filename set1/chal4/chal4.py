## big file that is XOR'd with one character
## same as last challenge. going to pick on string

## each line is a string. 
## wow cute, frequency analysis help cut this down by like 1000%
import binascii
import string

flag = ""
all_ascii = string.printable
common_english = "etaoinshrdlu"
raw = [] ## all the strings in the file converted to bytes
s = 0 


with open('4.txt', 'r') as file:
    content = file.read().split('\n')
    for x in content: 
        val = bytes.fromhex(x)
        raw.append(val)

for x in all_ascii:
    for bin_string in raw:     
        for y in bin_string:
            val = y ^ ord(x)
            flag += chr(val)
        for z in flag:
            z = z.lower()
            if z not in string.printable:
                break 
            elif common_english.find(z) != -1:
                s += 1      
        if (s > 16):
            print(flag, s, x, binascii.hexlify(bin_string).decode(), "\n")
        flag = ''
        s = 0

 
