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
from generic import find_inverse, is_prime, xgcd, gcd

# TODO: temos que alterar para usar um teste probabilistico ao invés de fatoracao por inteiros (prof. pediu)
prime_number_limit = 1000


class Rsa:
    def __init__(self):
        self.bits = 3
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

    def generate_prime(self, limit: int = 0, skip: int = 0) -> int:
        # números primos são valores inteiros maiores que 1
        # divisíveis apenas por 1 e por si mesmos

        # define maior limite entre prime_number_limit e parametro limit
        # limit = prime_number_limit if (limit > prime_number_limit) else limit
        # TODO Verificar se o uso do número de bits é considerado para o tamanho do primo
        # https://security.stackexchange.com/a/37910
        if limit > 0:
            # gera número aleatorio entre 2 e prime_number_limit
            number = random.randint(1, limit - 1)
        else:
            number = random.randint(2 ** (self.bits - 1), 2 ** (self.bits))

        # se for par, soma 1 para ser ímpar (pares não são primos, exceto 2)
        if (number % 2) == 0:
            number += 1

        # enquanto não for primo, soma dois e tenta novamente
        while not is_prime(number): 
            number = random.randint(1, limit - 1)
            # TODO verificar o motivo de +2, pq pode ser maior que o limit ocorrendo erro
            # number += 2

        # garante que p e q sejam números diferentes
        if skip == number:
            print("p é igual, tentando de novo")
            number = self.generate_prime(skip=skip)
        
        print('number', number)
        return number

    def generate_keypair(self, p: int, q: int) -> None:
        """
        p - número primo
        q - outro número primo
        """

        if not (is_prime(p) and is_prime(q)):
            raise ValueError("p e q devem ser primos para gerar a chave.")
        elif p == q:
            raise ValueError("p e q não podem ser iguais para gerar a chave.")

        # 2. calcule n pela equacao n = p*q
        n = p * q

        # 3. selecione um inteiro ímpar pequeno 'e' tal que ele seja primo em relacao
        # a phi(n) que, pela equacao é igual a (p-1)*(q-1)
        phi = (p - 1) * (q - 1)
        e = self.generate_prime(limit=phi)  # 13

        # Acha um inteiro "e" em que "e" e "phi" são coprimos
        while gcd(e, phi) != 1:
            print("Não é coprimo, tentando de novo.")
            e = self.generate_prime(limit=phi)

        self.p, self.q, self.e, self.phi, self.n = p, q, e, phi, n

        self.publicKey = [e, n]
        print('phi', phi)
        print('publicKey', [e, n])

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

        self.d = find_inverse(self.e, self.phi)
        self.privateKey = [self.d, self.n]
        print('e / phi', [self.e, self.phi])
        print('privateKey', self.privateKey)

        decrypted_message = ""

        for c in message:
            decoded_letter = pow(c, self.privateKey[0], self.privateKey[1])
            decoded_letter = str(chr(decoded_letter))
            decrypted_message += decoded_letter

        return decrypted_message

    @staticmethod
    def brutalForce(coded_message, pk):

        decrypted_message = ""

        p = 1
        q = 1

        e = pk[0]
        n = pk[1]

        nSqrt = math.sqrt(n)
        nControl = 3

        # dado n tenta descobrir p e q
        while nControl <= nSqrt:
            if (n % nControl) == 0:
                p = n // nControl
                q = nControl
                break
            nControl += 2

        phi = (p - 1) * (q - 1)

        d = find_inverse(e, phi)

        for c in coded_message:
            decoded_letter = pow(c, d, n)
            decoded_letter = str(chr(decoded_letter))
            decrypted_message += decoded_letter

        return decrypted_message
