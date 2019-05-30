"""
References:
    https://gist.github.com/AJamesPhillips/9570158
    https://www.youtube.com/watch?v=l9okvhYxtiU
    https://github.com/jacksjm/rsa-python/blob/master/brutalForce.py
    https://github.com/sybrenstuvel/python-rsa/blob/master/rsa/prime.py
    https://github.com/MatthewCLind/Crypto_Practice/blob/master/RSA_keygen.py
"""

def gcd(a, b):
    """
    Greatest common divisor
    """
    while b != 0:
        a, b = b, a % b
    return a

'''
Euclid's extended algorithm for finding the multiplicative inverse of two numbers
'''
def multiplicative_inverse(e, phi):
    return

def is_prime(number):
    """
    Test to see if a number is prime.
    """
    return True

def generate_keypair(p, q):
    """
    p - prime number
    q - another prime number
    """
    # you must use d = multiplicative_inverse(e, phi) and gcd(e, phi)
    return

def encrypt(pk, message):
    """
    pk - private key
    message - plain text to cipher
    """
    cipher = ''
    return cipher

def decrypt(pk, ciphertext):
    return
    
