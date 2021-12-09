from Crypto import Cipher
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import json
import pwn
from random import randint
import sys

if (len(sys.argv) == 1):
    print("Usage: python3 ./Solution.py $IP:$PORT")
    exit()
r = sys.argv[1].split(":")
ip = r[0]
port = int(r[1])
connection = pwn.remote(ip, port)

r = connection.recv()
r = r.decode()
r = r.split("\n")
flag = r[2]
plaintext = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
r =  '{"pt": "' + plaintext + '"}'
r = r.encode()
connection.send(r)
r = connection.recv()
ciphertext = r.decode()

def firstHalf(plaintext):
    alphabet = '0123456789abcdef'
    const = 'cyb3rXm45!@#'
    ret = {}
    pt = bytes.fromhex(plaintext)
    for a in alphabet:
        for b in alphabet:
            for c in alphabet:
                for d in alphabet:
                    key = a + b + c + d
                    key = const + key
                    key = key.encode()
                    cipher = AES.new(key, mode=AES.MODE_ECB)
                    ct = cipher.encrypt(pad(pt, 16))
                    ret[ct] = key
    return ret

def secondHalf(ciphertext, dictionaryOfCts):
    alphabet = '0123456789abcdef'
    const = 'cyb3rXm45!@#'
    ct = bytes.fromhex(ciphertext)
    for a in alphabet:
        for b in alphabet:
            for c in alphabet:
                for d in alphabet:
                    key = a + b + c + d
                    key = key + const
                    key = key.encode()
                    cipher = AES.new(key, mode=AES.MODE_ECB)
                    enc = cipher.decrypt(ct)
                    if (enc in dictionaryOfCts):
                        return dictionaryOfCts[enc], key

def solve(plaintext, ciphertext, flag):
    flag = bytes.fromhex(flag)
    dictionaryOfCts = firstHalf(plaintext)
    key1, key2 = secondHalf(ciphertext, dictionaryOfCts)
    enc = AES.new(key2, mode=AES.MODE_ECB)
    output = enc.decrypt(flag)
    enc = AES.new(key1, mode=AES.MODE_ECB)
    output = enc.decrypt(output)
    output = output.decode()
    output = output.split("\n")
    output = output[1].replace("\x0c", "")
    print(output)

solve(plaintext, ciphertext, flag)

