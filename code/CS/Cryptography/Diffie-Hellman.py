def diffie_hellman_key_exchange(p, g, a, b):
    """
    Performs a Diffie-Hellman key exchange.

    Arguments:
    p -- a prime number
    g -- a primitive root modulo p
    a -- Alice's private key
    b -- Bob's private key

    Returns:
    s -- the shared secret
    """
    # Alice computes A = g^a mod p and sends it to Bob
    A = pow(g, a, p)

    # Bob computes B = g^b mod p and sends it to Alice
    B = pow(g, b, p)

    # Alice computes s = B^a mod p
    s_Alice = pow(B, a, p)

    # Bob computes s = A^b mod p
    s_Bob = pow(A, b, p)

    # Both should arrive at the same s
    assert s_Alice == s_Bob

    return s_Alice

# Let's perform a key exchange with p=23, g=5, a=6, and b=15
p = 541
g = 10
a = 6
b = 8

shared_secret = diffie_hellman_key_exchange(p, g, a, b)

print("The shared secret is:", shared_secret)
