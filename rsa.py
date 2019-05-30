"""
References:
    https://gist.github.com/AJamesPhillips/9570158
    https://www.youtube.com/watch?v=l9okvhYxtiU
    https://github.com/jacksjm/rsa-python/blob/master/brutalForce.py
    https://github.com/sybrenstuvel/python-rsa/blob/master/rsa/prime.py
    https://github.com/MatthewCLind/Crypto_Practice/blob/master/RSA_keygen.py
"""
import random

class Rsa:
    def __init__(self):
        self.p = 0
        self.q = 0

    @staticmethod
    def gcd(a, b):
        """
        Greatest common divisor
        """
        while b != 0:
            a, b = b, a % b
        return a

    def generate_prime(self):
        # números primos são valores inteiros maiores que 1
        # divisíveis apenas por 1 e por si mesmos
        prime_number_limit = 1000
        # gera número aleatorio entre 2 e prime_number_limit
        number = random.randint(2,prime_number_limit)

        # se for par, soma 1 para ser ímpar (pares não são primos, exceto 2)
        if (number % 2) == 0:
            number += 1

        # enquanto não for primo, soma dois e tenta novamente
        while not self.is_prime(number):
            number += 2
            
        return number


    @staticmethod
    def is_prime(number):
        """
        Test to see if a number is prime.
        """

        is_prime = True 

        # tenta dividir pelos números a partir de 3 até sua metade, andando de 2 em 2
        for n in range(3, int(number/2)+2, 2):
            if (number % n) == 0:
                is_prime = False
                break
            
        return is_prime


    '''
    Euclid's extended algorithm for finding the multiplicative inverse of two numbers
    '''
    @staticmethod
    def multiplicative_inverse(e, phi):
        return

    @staticmethod
    def generate_keypair(p, q):
        """
        p - prime number
        q - another prime number
        """
        # you must use d = multiplicative_inverse(e, phi) and gcd(e, phi)

        return

    @staticmethod
    def encrypt(pk, message):
        """
        pk - private key
        message - plain text to cipher
        """
        cipher = ''
        return cipher

    @staticmethod
    def decrypt(pk, ciphertext):
        return
        
