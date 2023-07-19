phrase = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
key = b"ICE"
flag = ""

for i, x in enumerate(phrase):
    key_val = key[i % len(key)] #math that make it so that ICE will repeat over
    val = x ^ key_val
    flag += hex(val)[2:]    

print(flag)

##cool little maths to make ICE repeat over but using the phrases index placements
##to calculate the placings of the key "ICE" 
