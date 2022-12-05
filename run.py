import binascii as B
import pride as P
import app as A

val1 = A.arr
arr1 = bytes(val1, 'utf-8')

val2 = A.name
arr2 = bytes(val2, 'utf-8')

print(arr1)
print(arr2)
print(len(A.arr))

key1        = B.unhexlify(arr1)
plain1      = B.unhexlify(arr2)
cipher1     = P.Pride(key1)
encrypted1  = cipher1.encrypt(plain1)
# print(P.b2s(B.hexlify(encrypted1)))  # b2s so it works w/ python 2 and 3
encrypt_text= P.b2s(B.hexlify(encrypted1))
decrypted1  = cipher1.decrypt(encrypted1)
# print(P.b2s(B.hexlify(decrypted1)))
decrypt_text=P.b2s(B.hexlify(decrypted1))