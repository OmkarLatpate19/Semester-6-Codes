import math
import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)

def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def modInverse(e, phi_n):
    for d in range(1, phi_n):
        if ((e % phi_n) * (d % phi_n)) % phi_n == 1:
            return d
    return -1

def generateKey(p, q):
    if not (isPrime(p) and isPrime(q)):
        raise ValueError('Both numbers must be prime')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    
    # n = pq
    n = p * q

    # phi is totient of n
    phi = (p - 1) * (q - 1)

    # Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    # Use Euclid's Algorithm to verify that e and phi(n) are coprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    d = modInverse(e, phi)

    return (e, n), (d, n)

def char_to_num(char):
    # Convert character to its corresponding number from 1 to 52 for both uppercase and lowercase letters
    if char.isalpha():
        if char.islower():
            return ord(char) - ord('a') + 1
        else:
            return ord(char.lower()) - ord('a') + 27
    else:
        return 0  # Return 0 for non-alphabetic characters

def num_to_char(num):
    # Convert number to its corresponding character from 'a' to 'z' or 'A' to 'Z'
    if num > 0:
        if num <= 26:
            return chr(num + ord('a') - 1)
        else:
            return chr(num + ord('A') - 27)
    else:
        return ''  # Return empty string for non-positive numbers


def encrypt(pk, plaintext):
    key, n = pk

    cipher = [pow(char_to_num(char), key, n) for char in plaintext]

    # Convert cipher numbers to characters and join them into a single string
    return ''.join(num_to_char(num) for num in cipher)

def decrypt(pk, ciphertext):

    key, n = pk

    # Convert characters of ciphertext to numbers, decrypt each one, and join them into a single string
    aux = [num_to_char(pow(char_to_num(char), key, n)) for char in ciphertext]

    return ''.join(aux)

if __name__ == '__main__':
    
    p = int(input(" - Enter a prime number (17, 19, 23, etc): "))
    q = int(input(" - Enter another prime number (Not one you entered above): "))

    print(" - Generating your public / private key-pairs now . . .")

    public, private = generateKey(p, q)

    print(" - Your public key is ", public, " and your private key is ", private)

    message = input(" - Enter a message to encrypt with your public key: ")
    encrypted_msg = encrypt(public, message)

    print(" - Your encrypted message is: ", encrypted_msg)
    print(" - Decrypting message with private key ", private, " . . .")
    print(" - Your message is: ", decrypt(private, encrypted_msg))
