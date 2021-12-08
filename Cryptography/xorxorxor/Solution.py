#!/usr/bin/env python3
import pwn

f = open("/home/naturalt/CTF/xorxorxor/output.txt", "r")
f = f.read()
input = f.split(" ")[1]
print(input)

key = ["H", "T", "B", "{"]

for i in range(0, 2*len(key), 2):
    x = key[i//2].encode()
    y = bytes.fromhex(input[i:i+2])
    key[i//2] = pwn.xor(x, y)

def decrypt(cipher):
    plain = b''
    for i in range(0, len(cipher), 2):
        z = bytes.fromhex(cipher[i:i+2])
        plain += pwn.xor(key[(i//2)%len(key)], z)
    return plain


print(decrypt(input))

