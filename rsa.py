"""
References:
    https://gist.github.com/AJamesPhillips/9570158
    https://www.youtube.com/watch?v=l9okvhYxtiU
    https://github.com/jacksjm/rsa-python/blob/master/brutalForce.py
    https://github.com/sybrenstuvel/python-rsa/blob/master/rsa/prime.py
    https://github.com/MatthewCLind/Crypto_Practice/blob/master/RSA_keygen.py

    https://www.lambda3.com.br/2012/12/entendendo-de-verdade-a-criptografia-rsa-parte-ii/

    Euclides:
    http://nuitshell.blogspot.com/2014/07/algoritmo-estendido-de-euclides.html
"""
import random
import math
from generic import (
    find_inverse,
    is_prime,
    is_prime_fermat,
    is_prime_miller,
    gcd,
    brutal_force_sqrt,
    brutal_force_pollard_rho,
)


class Rsa:
    def __init__(self):
        self.bits = 4
        self.primeMethod = "brute"
        self.p = 0  # primeiro numero primo
        self.q = 0  # segundo numero primo
        self.n = 0  # representa o tamanho do conjunto (p*q)
        self.e = 0  # primo relativo de phi cujo gdc(e,phi) = 1
        self.phi = 0  # totiente

        self.publicKey = []  # chave publica
        self.privateKey = []  # chave privada

    def set_bits(self, bits) -> None:
        self.bits = bits
        return

    def set_prime_method(self, primeMethod="brute") -> None:
        self.primeMethod = primeMethod
        return

    def is_prime(self, n: int) -> bool:
        """
        Função para executar a função de verificação de número primo, utilizando
        a forma bruta, Fermat ou Miller
        """
        return (
            is_prime_miller(n)
            if self.primeMethod == "miller"
            else is_prime_fermat(n)
            if self.primeMethod == "fermat"
            else is_prime(n)
        )

    def generate_prime(self, limit: int = 0, ignore: int = 0) -> int:
        # números primos são valores inteiros maiores que 1
        # divisíveis apenas por 1 e por si mesmos

        # https://security.stackexchange.com/a/37910
        if limit > 0:
            # gera número aleatorio entre 2 e prime_number_limit
            number = random.randint(2 ** (self.bits - 1), limit - 1)
        else:
            number = random.randint(2 ** (self.bits - 1), 2 ** (self.bits) -1)

        # se for par, soma 1 para ser ímpar (pares não são primos, exceto 2)
        if (number != 2) and (number % 2) == 0:
            number += 1

        # enquanto não for primo, soma dois e tenta novamente
        while not self.is_prime(number):
            # print("number", number, limit)
            number += 2
            if limit > 0 & number > limit:
                number = random.randint(2 ** (self.bits - 1), limit - 1)

        # garante que p e q sejam números diferentes
        if ignore == number:
            # print("p é igual, tentando de novo")
            number = self.generate_prime(ignore=ignore)

        return number

    def generate_keypair(self, p: int, q: int) -> None:
        """
        p - número primo
        q - outro número primo
        """
        if not (self.is_prime(p) and self.is_prime(q)):
            raise ValueError("p e q devem ser primos para gerar a chave.")
        elif p == q:
            raise ValueError("p e q não podem ser iguais para gerar a chave.")

        # 2. calcule n pela equacao n = p*q
        n = p * q

        # 3. selecione um inteiro ímpar pequeno 'e' tal que ele seja primo em relacao
        # a phi(n) que, pela equacao é igual a (p-1)*(q-1)
        phi = (p - 1) * (q - 1)
        # https://crypto.stackexchange.com/questions/3110/impacts-of-not-using-rsa-exponent-of-65537
        e = self.generate_prime(limit=phi) # Deveria ser 65537 pelo padrão

        # Acha um inteiro "e" em que "e" e "phi" são coprimos
        while gcd(e, phi) != 1:
            # print("Não é coprimo, tentando de novo. e, phi", e, phi)
            e = self.generate_prime(limit=phi)

        self.p, self.q, self.e, self.phi, self.n = p, q, e, phi, n
        self.publicKey = [e, n]
        self.d = find_inverse(self.e, self.phi)
        self.privateKey = [self.d, self.n]

        return

    @staticmethod
    def encrypt(pk: list, message: str) -> list:
        """
        pk - private key
        message - plain text to cipher
        """

        crypted_message = []

        for c in message:
            ascii_code = ord(c)  # codigo ascii do caracter message
            coded_letter = pow(ascii_code, pk[0], pk[1])  # letra^e mod n
            crypted_message.append(coded_letter)

        return crypted_message

    def decrypt(self, message: list) -> str:

        decrypted_message = ""

        for c in message:
            decoded_letter = pow(c, self.privateKey[0], self.privateKey[1])
            decoded_letter = str(chr(decoded_letter))
            decrypted_message += decoded_letter

        return decrypted_message

    @staticmethod
    def brutalForce(coded_message: str, pk: list, method="brute") -> str:

        decrypted_message = ""
        e = pk[0]
        n = pk[1]

        if method == "pollard":
            d = brutal_force_pollard_rho(n, e)
        else:
            d = brutal_force_sqrt(n, e)
        
        for c in coded_message:
            decoded_letter = pow(c, d, n)
            decoded_letter = str(chr(decoded_letter))
            decrypted_message += decoded_letter

        return decrypted_message
