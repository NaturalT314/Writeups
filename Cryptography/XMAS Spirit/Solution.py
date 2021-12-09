import string
from math import gcd
import random

s = string.printable
f = open("./encrypted.bin", "rb").read()

input = bytes.hex(f)
mod = 256 
counter = 0
header = "%PDF-"
flagFormat = "HTB"
compare1 = input[:10]

for b in range(0,257):
    for a in range(1, 257, 2):
        compare2 = ""
        for letter in header:
            enc = (a*ord(letter) + b) % mod
            enc = str(hex(enc))[2:]
            if(len(enc) < 2):
                enc = '0' + enc
            compare2 = compare2 + enc
        if (compare1 == compare2):
            m = a
            c = b
            b = 300
            a  = 300

output = ""
for i in range(0, len(input), 2):
    charInHex = input[i:i+2]
    for j in range(0, 256):
        enc = (m*j + c) % mod
        enc = str(hex(enc))[2:]
        while(len(enc) < 2):
            enc = '0' + enc
        if (enc == charInHex):
            enc = str(hex(j))[2:]
            while(len(enc) < 2):
                enc = '0' + enc
            output = output + enc
            break

w = open("./Flag.pdf", "wb")
w.write(bytes.fromhex(output))