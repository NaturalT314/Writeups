#!/usr/bin/env python3
import pwn
import string

strings = string.printable

f = open("/home/naturalt/CTF/Cryptography/BabyEncryption/msg.enc", "r")
input = f.read()

output = ""

def map(p):
    c = ord(p)
    return (123 * c + 18) % 256


for i in range(0, len(input), 2):
    x = input[i:i+2]
    x = int(x, 16)
    for j in strings:
        if (x == map(j)):
            output = output + j
print(output)