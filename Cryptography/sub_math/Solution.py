from Crypto.Util.number import *
import string

def enc(t):
    return str(( 51415 & 5 + 314) | ord(t) << 15)

printableStrings = string.printable

cipher = open("./cipher.enc", "rb").read()
cipher = bytes_to_long(cipher)
cipher = str(cipher)

chars = []

#creating an array, each element is a 7 digit from cipher
for i in range(0, len(cipher), 7):
    chars.append(cipher[i:i+7])

output = []

for char in chars:
    for printableString in printableStrings:
        if (enc(printableString) == char):
            output.append(printableString)

output = "".join(output)

print(output)