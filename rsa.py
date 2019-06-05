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



def xgcd(a: int,b: int) -> int:

    if b == 0:
        return [1,0,a]
    else:
        x,y,d = xgcd(b, a%b)
    
    return [y,x-(a//b)*y,d]



class Rsa:
    def __init__(self):

        self.p = 0 #primeiro numero primo
        self.q = 0 #segundo numero primo
        self.n = 0 #representa o tamanho do conjunto (p*q)
        self.e = 0 #primo relativo de phi cujo gdc(e,phi) = 1
        self.phi = 0 #totiente

        self.publicKey = [] #chave publica
        self.privateKey =[] #chave privada

        self.q = 17#self.generate_prime() #17
        self.p = 41#self.generate_prime(skip=self.q) #41

        self.generate_keypair(self.p, self.q)


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
            #print("p é igual, tentando de novo")
            return self.generate_prime(skip=skip)

        return number


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
        e = 13#self.generate_prime(limit=phi) #13

        # Acha um inteiro "e" em que "e" e "phi" são coprimos
        while ( gcd(e, phi) != 1):
            print("Não é coprimo, tentando de novo.")
            e = self.generate_prime(limit=phi)

        self.p, self.q, self.e, self.phi, self.n = p, q, e, phi, n

        self.publicKey = [e,n]
        
        return


    @staticmethod
    def encrypt(pk: list, message: str) -> str:
        """
        pk - private key
        message - plain text to cipher
        """

        crypted_message = []

        for c in message:
            ascii_code = ord(c) #codigo ascii do caracter message
            coded_letter = pow(ascii_code, pk[0], pk[1]) #letra^e mod n
            crypted_message.append(coded_letter)

        return crypted_message


    def decrypt(self, message: list) -> None:

        euclides_array = xgcd(self.e, self.phi)
        self.privateKey = [euclides_array[0],self.n]
        
        decrypted_message = ''

        for c in message:
            decoded_letter = pow(c,self.privateKey[0],self.privateKey[1])
            decoded_letter = str(chr(decoded_letter))
            decrypted_message += decoded_letter

        return decrypted_message


