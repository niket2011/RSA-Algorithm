# RSA-Algorithm
Key Generation –
Choose two different large prime numbers p and q.
Calculate n = p*q, where n is the modulus for the public key and the private keys.
Calculate the totient: Φ(n) = (p-1)(q-1).
Choose an integer e such that 1< e < Φ(n), and e is co-prime to Φ(n);
Gcd (e, Φ(n)) = 1. e is released as the public key exponent
Compute the secret exponent d, 1< d < Φ(n), such that e*d = 1 mod Φ(n).
d = (k * Φ(n) +1) / e  for some integer k.
The public key is (n, e) and the private key (n, d). Keep all the values d, p, q and Φ(n) secret. 
Encrypting Message – 
Obtains the recipient’s public key (n, e).
Represent the plaintext message as a positive integer m with 1< m < n.
Compute the ciphertext c = me mod n
Send the ciphertext c.
Decrypting Message – 
Use the private key (n, d) to compute m = cd mod n.
Extracts the plaintext from the message representative m
