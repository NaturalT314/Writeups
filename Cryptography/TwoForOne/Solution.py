import gmpy2
from Crypto.Util.number import *
import json
import ast
from Crypto.PublicKey import RSA
from rsa import key
import base64


key1 = open("/home/naturalt/CTF/Cryptography/TwoForOne/key1.pem", "r").read()
key2 = open("/home/naturalt/CTF/Cryptography/TwoForOne/key2.pem", "r").read()
message1 = open("/home/naturalt/CTF/Cryptography/TwoForOne/message1", "r").read()
message1 = base64.b64decode(message1)
message1 = bytes_to_long(message1)
message2 = open("/home/naturalt/CTF/Cryptography/TwoForOne/message2", "r").read()
message2 = base64.b64decode(message2)
message2 = bytes_to_long(message2)

key1 = RSA.importKey(key1)
key2 = RSA.importKey(key2)

def egcd(a, b):
  if (a == 0):
    return (b, 0, 1)
  else:
    g, y, x = egcd(b % a, a)
    return (g, x - (b // a) * y, y)

# Calculates a^{b} mod n when b is negative
def neg_pow(a, b, n):
	assert b < 0
	assert GCD(a, n) == 1
	res = int(gmpy2.invert(a, n))
	res = pow(res, b*(-1), n)
	return res

# e1 --> Public Key exponent used to encrypt message m and get ciphertext c1
# e2 --> Public Key exponent used to encrypt message m and get ciphertext c2
# n --> Modulus
# The following attack works only when m^{GCD(e1, e2)} < n
def common_modulus(e1, e2, n, c1, c2):
	g, a, b = egcd(e1, e2)
	if a < 0:
		c1 = neg_pow(c1, a, n)
	else:
		c1 = pow(c1, a, n)
	if b < 0:
		c2 = neg_pow(c2, b, n)
	else:
		c2 = pow(c2, b, n)
	ct = c1*c2 % n
	m = int(gmpy2.iroot(ct, g)[0])
	return long_to_bytes(m)

output = common_modulus(key1.e, key2.e, key1.n, message1, message2)
output = output.decode()

print(output)