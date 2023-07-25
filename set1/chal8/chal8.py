import itertools
from binascii import a2b_hex

with open('8.txt','r') as file:
    content = file.read().strip()
    
chunks = [content[x:x+16] for x in range(0, len(content), 16)]
pairs = itertools.combinations(chunks,2)

for x in pairs:
    if (x[0] == x[1]):
        print(x)