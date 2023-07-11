import math
import random

def calculate_phi(p, q):
    """
    Calculates the Euler's totient function for p*q.
    """
    return (p - 1) * (q - 1)



def rsa_key_generation(n_bits=512):
    """
    Generates the public and private keys for the RSA algorithm.
    """
    # Step 1: Generate two different large random prime numbers p and q.
    p = generate_prime_number(n_bits)
    q = generate_prime_number(n_bits)
    while p == q:
        q = generate_prime_number(n_bits)
    
    # Step 2: Compute n = p*q. n is the modulus for both the public and private keys.
    n = p * q

    # Step 3: Compute the totient phi = (p-1)*(q-1).
    phi = calculate_phi(p, q)

    # Step 4: Choose an integer e such that 1 < e < phi and gcd(e, phi) = 1; e is the public key exponent.
    e = 3
    while math.gcd(e, phi) != 1:
        e += 2

    # Step 5: Compute the private key d.
    d = pow(e, -1, phi)

    return (e, n), (d, n)  # public and private keys



def rsa_encrypt(message, public_key):
    """
    Encrypts a message using the RSA algorithm and a public key.
    """
    e, n = public_key
    cipher_text = [pow(ord(char), e, n) for char in message]
    return cipher_text



def rsa_decrypt(cipher_text, private_key):
    """
    Decrypts a cipher text using the RSA algorithm and a private key.
    """
    d, n = private_key
    message = ''.join([chr(pow(char, d, n)) for char in cipher_text])
    return message



def generate_prime_number(n_bits=32):
    """
    Generates a prime number with n_bits bits.
    """
    while True:
        p = random.getrandbits(n_bits)
        if is_prime(p):
            return p



def is_prime(num):
    """
    Checks if a number is prime.
    """
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2
    return True

# Generate a pair of keys (public and private)
public_key, private_key = rsa_key_generation(n_bits=32)

# Define a message
message = input("Input a message to encrypt: ")

# Encrypt the message
encrypted_message = rsa_encrypt(message, public_key)

# Decrypt the message
decrypted_message = rsa_decrypt(encrypted_message, private_key)

# Print the results
print("Original message:", message)
print("Encrypted message:", encrypted_message)
print("Decrypted message:", decrypted_message)