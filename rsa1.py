import random
import math
def Encrypt(asc,e,n):
	a=(asc**e)%n
	return a
def Decrypt(b,d,n):
	q=(b**d)%n
	return q

p=int(input("Enter the first large number"))
q=int(input("Enter the second large number"))
n=p*q
phi=(p-1)*(q-1)
arrofe=[]
e=2
while(e<phi):
	if(math.gcd(e,phi)==1 and n%e!=0):
		arrofe.append(e)
		e+=1
	else:
		e+=1
print("List of e values is ",arrofe)
e=random.choice(arrofe)
print("e selected is",e)
d=1
while(1):
	if(((e*d)%phi)==1):
		print("Value of d is:",d)
		break
	else:
		d+=1
encryption=[]
decryption=[]
pt=str(input("Enter the plain text"))
for x in pt:
	encryption.append(Encrypt(ord(x),e,n))
print("Cipher text is",encryption)
for x in encryption:
	decryption.append(Decrypt(x,d,n))
print("Decipher text is",decryption)
print("The final decrypted text is:",end='')
for x in decryption:
	print(chr(int(x)),end='')	

		





