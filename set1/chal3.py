## single byte XOR 
## encoded string has been XOR with a random single character
import string 

flag = ""
all_ascii = string.printable
common_english = "etaoinshrdlu"

hex_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

## decode the string to raw bytes, ascii 
raw = bytes.fromhex(hex_string)
s = 0 

for x in all_ascii:
    for y in raw:
        val = y ^ ord(x) ## ord gives you the ascii rep of string
        flag += chr(val) ## chr() turns decimal back to ascii
    
    #perform frequency analysis here, count how many common
    #english words there are 
    for z in flag:
        z = z.lower()
        if z not in string.printable:
            break 
        if common_english.find(z) != -1:
            s += 1 
    
    if (s > 15):
        print(flag, s, x)
    flag = "" ## reset the flag, clear it up bb
    s = 0