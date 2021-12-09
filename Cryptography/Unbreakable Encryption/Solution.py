import pwn
ct1 = "4fd098298db95b7f1bc205b0a6d8ac15f1f821d72fbfa979d1c2148a24feaafdee8d3108e8ce29c3ce1291"
ct2 = "41d9806ec1b55c78258703be87ac9e06edb7369133b1d67ac0960d8632cfb7f2e7974e0ff3c536c1871b"
pt1 = b"hey let's rob the bank at midnight tonight!"
pt2 = ""
key = ""

ct1 = bytes.fromhex(ct1)
key = pwn.xor(ct1, pt1)
ct2 = bytes.fromhex(ct2)
pt2 = str(pwn.xor(ct2, key))
pt2 = pt2[10:-5]
print(pt2)
