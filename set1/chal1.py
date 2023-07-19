## convert hex to base64
## always operate in raw bytes, never use encoded strings
## this string is encoded in hex. must decode first. 
string1 = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
raw_bytes = bytes.fromhex(string1).decode("ascii")

## string: I'm killing your brain like a poisonous mushroom
## use terminal command: echo <string> | base64
## thus, SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29tCg==
