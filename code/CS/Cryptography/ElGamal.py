def elgamal_key_generation(p, g, a):
    """
    Generates the public and private keys for the ElGamal algorithm.

    Arguments:
    p -- a prime number
    g -- a generator of the multiplicative group of integers modulo p
    a -- the private key

    Returns:
    (p, g, h) -- the public key
    a -- the private key
    """
    h = pow(g, a, p)
    return (p, g, h), a

def elgamal_encrypt(m, public_key, k):
    """
    Encrypts a message using the ElGamal algorithm and a public key.

    Arguments:
    m -- the message (as an integer)
    public_key -- the public key
    k -- a random integer

    Returns:
    c -- the ciphertext
    """
    p, g, h = public_key
    c1 = pow(g, k, p)
    c2 = (m * pow(h, k, p)) % p
    return c1, c2

def elgamal_decrypt(c, private_key, public_key):
    """
    Decrypts a ciphertext using the ElGamal algorithm and a private key.

    Arguments:
    c -- the ciphertext
    private_key -- the private key
    public_key -- the public key

    Returns:
    m -- the message
    """
    c1, c2 = c
    p, _, _ = public_key
    a = private_key
    m = (c2 * pow(c1, p - 1 - a, p)) % p
    return m

# Let's perform an encryption and decryption with example figures for p, g, a, m, and k
p = 541
g = 14
a = 6
m = 20
k = 3

# Generate keys
public_key, private_key = elgamal_key_generation(p, g, a)

# Encrypt the message
ciphertext = elgamal_encrypt(m, public_key, k)

# Decrypt the message
decrypted_message = elgamal_decrypt(ciphertext, private_key, public_key)

# Print the results
print("Original message:", m)
print("Ciphertext:", ciphertext)
print("Decrypted message:", decrypted_message)
