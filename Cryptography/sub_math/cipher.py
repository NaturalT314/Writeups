from Crypto.Util.number import *
flag = open('flag.txt','r').read()
def enc(flag):
    return''.join([str((( 51415 & 5 + 314) | ord(t) << 15 ))  for t in flag ])   
cipher = long_to_bytes(enc(flag))
b = open("cipher.enc","wb")
b.write(cipher)
b.close()
