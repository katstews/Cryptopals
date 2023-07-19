## fixed XOR
val1 = "1c0111001f010100061a024b53535009181c"
val2 = "686974207468652062756c6c277320657965"
flag = ""

if (len(val1) == len(val2)):
    ## perform XOR operation
    for x in range(len(val1)):
            #this converts hex to its corresponding decimal value  
        val = int(val1[x],16) ^ int(val2[x],16) #16 to tell int() were converting hex values
        flag = flag + format(val, 'x') #format val (decimal) to hex string
else:
    print("invalid length")

print(flag)
## flag = 746865206b696420646f6e277420706c6179
## correct!