## 1 char = 1 byte lord, 8 bits for one character 
# string1 = b"this is a test"
# string2 = b"wokka wokka!!!"
import string
import base64

common_english = "etaoinshrdlu"
allchar = string.printable

with open("6.txt","rb") as file:
    content = file.read()

binarystring = []
content = base64.b64decode(content)
for x in content:
    val = format(x,'08b')
    binarystring.append(val)

############################# find the keysize ######################
def hamming_distance(str1,str2):
    hamming = 0
    #calculate hamming distance 
    for val1, val2 in zip(str1,str2):
        if val1 != val2:
            hamming += 1 
    return hamming   

hamval = []
total_size = []

for KEYSIZE in range(2, 40):
    for x in range(0, len(binarystring), KEYSIZE):
        chunk1 = binarystring[x:x+KEYSIZE] 
        chunk2 = binarystring[x+KEYSIZE:x+2*KEYSIZE] 
        chunk1 = ''.join(chunk1)
        chunk2 = ''.join(chunk2)
        # print(chunk1,chunk2)
        val = hamming_distance(chunk1,chunk2) 
        adjusted = val/KEYSIZE   
        hamval.append(adjusted)
    average = sum(hamval) / len(hamval)
    total_size.append(('total:', average, "keysize:", KEYSIZE))
    hamval.clear()

sorted_data = sorted(total_size, key=lambda x: x[1])
#################################### keysize #####################

################# find the key ####################################
### keysize = 29
byte_block = []

for x in range(0, len(binarystring), 29):
    val = binarystring[x:x+29]
    byte_block.append(val)

for x in range(24):
    byte_block[99].append('00000000')

flag = []

for y in range(29):
    val = []
    for x in range(len(byte_block)):
        val.append(byte_block[x][y])
    flag.append(val)

final_damn_flag = [] 

for z in range(29):
    guesses = []
    for y in allchar:
        guess = []
        for x in flag[z]:
            val = int(x,2) ^ ord(y)   
            guess.append(chr(val))
        guesses.append((''.join(guess),y))
    maxval = []
    for x in guesses:
        vals = []
        s = 0
        for y in x[0]:
            if y in common_english:
                s+=1
        maxval.append((s,x[1]))
        
    final_damn_flag.append(max(maxval)[1])

final_damn_flag = ''.join(final_damn_flag)

final = []

for i, x in enumerate(binarystring):
    key_val = final_damn_flag[i % len(final_damn_flag)] #math that make it so that ICE will repeat over
    val = int(x,2) ^ ord(key_val)
    final.append(chr(val))

##################### print the flags ##########################
print("The key:", final_damn_flag, "\n")
print(''.join(final))