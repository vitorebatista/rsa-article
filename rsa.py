"""
References:
    https://gist.github.com/AJamesPhillips/9570158
    https://www.youtube.com/watch?v=l9okvhYxtiU
    https://github.com/jacksjm/rsa-python/blob/master/brutalForce.py
    https://github.com/sybrenstuvel/python-rsa/blob/master/rsa/prime.py
    https://github.com/MatthewCLind/Crypto_Practice/blob/master/RSA_keygen.py

    Euclides:
    http://nuitshell.blogspot.com/2014/07/algoritmo-estendido-de-euclides.html
"""
import random

prime_number_limit = 1000

# TODO: temos que alterar para usar um teste probabilistico ao invés de fatoracao por inteiros (prof. pediu)


def is_prime(number: int) -> int:
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


class Rsa:
    def __init__(self):
        self.p = 0
        self.q = 0
        self.e = 0
        self.n = 0
        self.phi = 0

    @staticmethod
    def gcd(a: int, b: int) -> int:
        """
        Greatest common divisor
        """
        # o algoritmo de Euclides recebe dois valores para os quais se deseja calcular o
        # maximo divisor comum (maior número que é divisível pelos dois valores) e realiza
        # divisoes sucessivas até encontrar o último resto não nulo desse processo
        # ex: a/b = q1 (r1 sendo div)
        #     b/r1 = q2 (r2 sendo mod)
        #     r1/r2 = q3 (r3 sendo mod)
        #     [...] mdc(a,b) = rn
        while (b > 0):
            q = int(a/b)  # calcula o resultado inteiro da divisao
            r = (a % b)  # calcula o resto da divisao
            a = b
            b = r

        # while b != 0:
        #    a, b = b, a % b

        return a

    def generate_prime(self, limit: int = prime_number_limit, skip: int = 0, ) -> int:
        # números primos são valores inteiros maiores que 1
        # divisíveis apenas por 1 e por si mesmos

        # define maior limite entre prime_number_limit e parametro limit
        limit = prime_number_limit if (limit > prime_number_limit) else limit

        # gera número aleatorio entre 2 e prime_number_limit
        number = random.randint(2, limit)

        # se for par, soma 1 para ser ímpar (pares não são primos, exceto 2)
        if (number % 2) == 0:
            number += 1

        # enquanto não for primo, soma dois e tenta novamente
        while not is_prime(number):
            number += 2

        # garante que p e q sejam números diferentes
        if (skip == number):
            print("p é igual, tentando de novo")
            return self.generate_prime(skip=skip)

        return number

    '''
    Euclid's extended algorithm for finding the multiplicative inverse of two numbers
    '''
    @staticmethod
    def multiplicative_inverse(e: int, phi: int) -> int:
        return 1

    def generate_keypair(self, p: int, q: int) -> int:
        """
        p - número primo
        q - outro número primo
        """
        if not (is_prime(p) and is_prime(q)):
            raise ValueError('p e q devem ser primos para gerar a chave.')
        elif p == q:
            raise ValueError('p e q não podem ser iguais para gerar a chave.')

        # 2. calcule n pela equacao n = p*q
        n = p * q

        # 3. selecione um inteiro ímpar pequeno 'e' tal que ele seja primo em relacao
        # a phi(n) que, pela equacao é igual a (p-1)*(q-1)
        phi = (p-1)*(q-1)
        e = self.generate_prime(limit=phi)

        # Acha um inteiro "e" em que "e" e "phi" são coprimos
        while (self.gcd(e, phi) != 1):
            print("Não é coprimo, tentando de novo.")
            e = self.generate_prime(limit=phi)

        self.p, self.q, self.e, self.phi, self.n = p, q, e, phi, n
        return 1

    @staticmethod
    def encrypt(pk, message: str) -> str:
        """
        pk - private key
        message - plain text to cipher
        """
        cipher = ''
        return cipher

    @staticmethod
    def decrypt(pk: int, ciphertext: str) -> None:
        return

    @staticmethod
    def xmdc(a: int, b: int) -> list:
        if b == 0:
            return [1, 0, a]
        else:
            x, y, d = Rsa.xmdc(b, a % b)
            return [y, x-(a//b)*y, d]