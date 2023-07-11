# SHA-256 implementation in Python
# Bitwise operations and logical functions

# Logical functions for SHA-256

def Ch(x, y, z):
    return (x & y) ^ (~x & z)

def Maj(x, y, z):
    return (x & y) ^ (x & z) ^ (y & z)

def Sigma0(x):
    return rotr(x, 2) ^ rotr(x, 13) ^ rotr(x, 22)

def Sigma1(x):
    return rotr(x, 6) ^ rotr(x, 11) ^ rotr(x, 25)

def sigma0(x):
    return rotr(x, 7) ^ rotr(x, 18) ^ shr(x, 3)

def sigma1(x):
    return rotr(x, 17) ^ rotr(x, 19) ^ shr(x, 10)

# Bitwise rotation and shift operations for 32-bit words

def rotr(x, n):
    return (x >> n) | (x << (32 - n)) & 0xFFFFFFFF

def shr(x, n):
    return x >> n


def sha256(message):
    # Constants
    K = [
        0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
        0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
        0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
        0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
        0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
        0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
        0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
        0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
    ]

    H = [
        0x6a09e667,
        0xbb67ae85,
        0x3c6ef372,
        0xa54ff53a,
        0x510e527f,
        0x9b05688c,
        0x1f83d9ab,
        0x5be0cd19
    ]

    # Pre-processing: Padding the message
    L = len(message) * 8  # Bit length of the message
    message += b'\x80'  # Append "1" bit to the end of the message
    message += b'\x00' * ((56 - len(message) % 64) % 64)  # Padding with "0" bits
    message += L.to_bytes(8, 'big')  # Append length of the original message in bits

    # Process the message in successive 64-bit chunks
    for i in range(0, len(message), 64):
        w = [0] * 64
        chunk = message[i:i+64]  # Get the next 64-bit chunk
        w[0:16] = [int.from_bytes(chunk[j:j+4], 'big') for j in range(0, 64, 4)]

        # Extend the first 16 words into the remaining 48 words of "message schedule" array
        for j in range(16, 64):
            w[j] = (sigma1(w[j-2]) + w[j-7] + sigma0(w[j-15]) + w[j-16]) & 0xFFFFFFFF

        # Initialize working variables to current hash value
        a, b, c, d, e, f, g, h = H

        # Compression function main loop
        for j in range(64):
            T1 = h + Sigma1(e) + Ch(e, f, g) + K[j] + w[j]
            T2 = Sigma0(a) + Maj(a, b, c)
            h = g
            g = f
            f = e
            e = (d + T1) & 0xFFFFFFFF
            d = c
            c = b
            b = a
            a = (T1 + T2) & 0xFFFFFFFF

        # Add this chunk's hash to result so far
        H[0] = (a + H[0]) & 0xFFFFFFFF
        H[1] = (b + H[1]) & 0xFFFFFFFF
        H[2] = (c + H[2]) & 0xFFFFFFFF
        H[3] = (d + H[3]) & 0xFFFFFFFF
        H[4] = (e + H[4]) & 0xFFFFFFFF
        H[5] = (f + H[5]) & 0xFFFFFFFF
        H[6] = (g + H[6]) & 0xFFFFFFFF
        H[7] = (h + H[7]) & 0xFFFFFFFF

    # Produce the final hash value (big-endian) as a 160 bit number, hex formatted
    return '%08x%08x%08x%08x%08x%08x%08x%08x' % (H[0], H[1], H[2], H[3], H[4], H[5], H[6], H[7])


# Test the function
message = input("Input message: ").encode()
sha256_hash = sha256(message)
print("SHA-256 Hash of the message is:", sha256_hash)
