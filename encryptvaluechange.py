mes=input()
encrypt=""
decrypt=""
j=0
for i in mes:
    encrypt+=chr(ord(i)+j)
    j+=1
print(encrypt)
j=0
for k in encrypt:
    decrypt+=chr(ord(k)-j)
    j+=1
print(decrypt)