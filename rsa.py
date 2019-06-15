import random
import math
from generic import (
    find_inverse,
    is_prime,
    is_prime_fermat,
    is_prime_miller,
    gcd,
    brutal_force,
    pollard_rho,
)

class Rsa:
    def __init__(self):
        self.bits = 4
        self.encryptMethod = "fermat"
        self.breakMethod = "brute"
        self.p = 0  # primeiro numero primo
        self.q = 0  # segundo numero primo
        self.n = 0  # representa o tamanho do conjunto (p*q)
        self.e = 0  # primo relativo de phi cujo gdc(e,phi) = 1, chave publica
        self.d = 0  # inverso multiplicativo de e, chave privada
        self.phi = 0  # totiente

        self.publicKey = []  # chave publica
        self.privateKey = []  # chave privada

    def set_bits(self, bits) -> None:
        """
        Configura o número de bits com que a classe vai trabalhar
        """
        self.bits = bits

    def set_EncryptMethod(self, encryptMethod="fermat") -> None:
        """
        Define o método para teste de primalidade:
        miller ou fermat
        """
        self.encryptMethod = encryptMethod
    
    def set_BreakMethod(self, breakMethod="brute") -> None:
        """
        Define o método para quebra de chave:
        pollard, brute
        """
        self.breakMethod = breakMethod

    def is_prime(self, n: int) -> bool:
        """
        Função para executar a função de verificação de número primo, utilizando
        a forma bruta, Fermat ou Miller
        """
        return (
            is_prime_miller(n)
            if self.encryptMethod == "miller"
            else is_prime_fermat(n)
        )

    def generate_prime(self, limit: int = 0, ignore: int = 0) -> int:
        # números primos são valores inteiros maiores que 1
        # divisíveis apenas por 1 e por si mesmos

        if limit > 0:
            # gera número aleatorio entre 2 e prime_number_limit
            number = random.randint(2 ** (self.bits - 1), limit - 1)
        else:
            number = random.randint(2 ** (self.bits - 1), 2 ** (self.bits) - 1)

        # se for par, soma 1 para ser ímpar (pares não são primos, exceto 2)
        if (number != 2) and (number % 2) == 0:
            number += 1

        # enquanto não for primo, soma dois e tenta novamente
        while not self.is_prime(number):
            number += 2
            if limit > 0 & number > limit:
                number = random.randint(2 ** (self.bits - 1), limit - 1)

        # garante que p e q sejam números diferentes
        if ignore == number:
            number = self.generate_prime(ignore=ignore)

        return number

    def generate_keypair(self, p: int, q: int) -> None:
        """
        Recebe p e q e realiza as operacoes para gerar as chaves criptograficas.
        p - número primo
        q - outro número primo
        """
        if not (self.is_prime(p) and self.is_prime(q)):
            raise ValueError("p e q devem ser primos para gerar a chave.")
        elif p == q:
            raise ValueError("p e q não podem ser iguais para gerar a chave.")

        # 2. calcula n pela equacao n = p*q
        n = p * q

        # 3. seleciona um inteiro ímpar pequeno 'e' tal que ele seja primo em relacao
        # a phi(n) que, pela equacao é igual a (p-1)*(q-1)
        phi = (p - 1) * (q - 1)
        # https://crypto.stackexchange.com/questions/3110/impacts-of-not-using-rsa-exponent-of-65537
        e = self.generate_prime(limit=phi)  # Poderia ser 65537 por padrão

        # Acha um inteiro "e" em que "e" e "phi" são coprimos
        while gcd(e, phi) != 1:
            e = self.generate_prime(limit=phi)

        self.p, self.q, self.e, self.phi, self.n = p, q, e, phi, n
        self.publicKey = [e, n]
        self.d = find_inverse(self.e, self.phi)
        self.privateKey = [self.d, self.n]

        return

    @staticmethod
    def encrypt(pk: list, message: str) -> list:
        """
        Criptografa uma string a partir de uma chave publica RSA, utilizando
        por base uma conversao para a tabela ASCII
        pk - chave publica
        message - texto para criptografar
        """
        crypted_message = []

        for c in message:
            ascii_code = ord(c)  # codigo ascii do caracter message
            coded_letter = pow(ascii_code, pk[0], pk[1])  # letra^e mod n
            crypted_message.append(coded_letter)

        return crypted_message

    def decrypt(self, message: list) -> str:
        """
        Descriptografa uma mensagem utilizando a chave privada RSA, tendo
        por base uma conversao da tabela ASCII
        pk - chave privada
        message - texto para descriptografar
        """
        decrypted_message = ""

        for c in message:
            decoded_letter = pow(c, self.privateKey[0], self.privateKey[1])
            decoded_letter = str(chr(decoded_letter))
            decrypted_message += decoded_letter

        return decrypted_message

    def breakMessage(self, coded_message: str, pk: list) -> str:
        """
        Realiza a quebra da chave publica
        coded_message - mensagem criptografada
        pk - chave publica
        """
        decrypted_message = ""
        e = pk[0]
        n = pk[1]

        if self.breakMethod == "pollard":
            d = pollard_rho(n, e)
        else:
            d = brutal_force(n, e)

        for c in coded_message:
            decoded_letter = pow(c, d, n)
            decoded_letter = str(chr(decoded_letter))
            decrypted_message += decoded_letter

        return decrypted_message
