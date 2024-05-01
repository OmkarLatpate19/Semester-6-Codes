import math
import random

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)
    
def char_to_num(char):
    return ord(char.lower()) - ord('a')+1

def num_to_char(num):
    return chr((num-1)%26+ord('a'))

p = int(input("Enter the 1st Prime No. : "))
q = int(input("Enter the 2nd Prime No. : "))

if is_prime(p) and is_prime(q):
    n = p * q
    print("n =", n)

    if is_prime(n):
        phi_n = n - 1
    else:
        phi_n = (p - 1) * (q - 1)
    print("Phi(n) =", phi_n)

    e = random.randint(2,phi_n-1)
    while gcd(e,phi_n)!=1:
        e = random.randint(2,phi_n-1)
        
    print("Generated value of e is : ",e)
    print("Calculating the value of d")
    d = pow(e, -1, phi_n)
    print("d =", d)

    public_key = {'e': e, 'n': n}
    print("\nPublic key is : {", end="")
    for key, value in public_key.items():
        print(key, ":", value, end="")
        if key != 'n':
            print(",", end=" ")
        else:
            print("}")

    private_key = {'d': d, 'n': n}
    print("\nPrivate key is : {", end="")
    for key, value in private_key.items():
        print(key, ":", value, end="")
        if key != 'n':
            print(",", end=" ")
        else:
            print("}")
            
    message=input("Enter the plaintext message : ")
    
    #Encyption
    encrypted_mesage=[]
    encrypted_characters=[]
    
    for char in message:
        if char.isalpha():
            num=char_to_num(char)
            encrypted_num=pow(num,e,n)
            encrypted_mesage.append(encrypted_num)
            encrypted_characters.append(num_to_char(encrypted_num))
            
    print("Encrypted message (characters) : ", ''.join(encrypted_characters))
    
    
    #Decryption
    decrypted_message=""
    for encrypted_num in encrypted_mesage:
        decrypted_num=pow(encrypted_num,d,n)
        decrypted_char=num_to_char(decrypted_num)
        decrypted_message+=decrypted_char
        
    print("Decrypted message : ",decrypted_message)

    '''plaintext = input("Enter the plaintext: ")

    # Convert string to ASCII
    plaintext_ascii = [ord(char) for char in plaintext]

    print("\nPerforming Encryption of Plaintext M from the formula : C = M^e mod n\n")
    # Encryption: C = M^e mod n
    encrypted_message = [pow(char, e, n) for char in plaintext_ascii]
    print("Encrypted message (C) =", encrypted_message)

    print("\nPerforming Decryption of Ciphertext C from the formula : M = C^d mod n\n")
    # Decryption: M = C^d mod n
    decrypted_ascii = [pow(char, d, n) for char in encrypted_message]


    # Convert ASCII to characters
    decrypted_message = ''.join([chr(char) for char in decrypted_ascii])
    print("Decrypted message (M) =", decrypted_message)'''

else:
    print("One or both of the entered numbers are not prime.")