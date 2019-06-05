import random

class rsaMath:

    @staticmethod
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


    @staticmethod
    def xgcd(a: int, b: int) -> list:

        if b == 0:
            return [1,0,a]
        else:
            x,y,d = rsaMath.xgcd(b, a%b)
        
        return [y,x-(a//b)*y,d]


