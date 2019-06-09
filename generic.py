import random
import math

def is_prime(number: int) -> bool:
    """
    Test to see if a number is prime.
    """
    if number == 2 or number == 3:
        return True

    if number < 2 or number % 2 == 0:
        return False

    # tenta dividir pelos números a partir de 3 até sua metade, andando de 2 em 2
    for n in range(3, int(math.sqrt(number))+1,1):
        if (number % n) == 0:
            return False

    return True


def is_prime_fermat(number: int, k=20) -> bool:
    # https://gist.github.com/Ayrx/5884802
    # Implementation uses the Fermat Primality Test

    # If number is even, it's a composite number

    if number == 2 or number == 3:
        return True

    if number % 2 == 0:
        return False

    for i in range(k):
        a = random.randint(1, number - 1)
        # https://stackoverflow.com/questions/32738637/calculate-mod-using-pow-function-python
        # https://www.khanacademy.org/computing/computer-science/cryptography/random-algorithms-probability/v/fermat-primality-test-prime-adventure-part-10
        if pow(a, number - 1, number) != 1:
            return False
    return True

def is_prime_miller(num: int):
    
    def miller(num: int):
        s = num - 1
        t = 0

        while s % 2 == 0:
            s = s // 2
            t += 1

        for trials in range(1):
            a = random.randrange(2, num - 1)
            v = pow(a, s, num)
            if v != 1:
                i = 0
                while v != (num - 1):
                    if i == t - 1:
                        return False
                    else:
                        i = i + 1
                        v = (v ** 2) % num
        return True
    
    if (num < 2):
        return False

    lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
                61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127,
                131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191,
                193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257,
                263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331,
                337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401,
                409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467,
                479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563,
                569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631,
                641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709,
                719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797,
                809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877,
                881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967,
                971, 977, 983, 991, 997]

    if num in lowPrimes:
        return True

    for prime in lowPrimes:
        if (num % prime) == 0:
            return False

    return miller(num)

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
    while b > 0:
        q = int(a / b)  # calcula o resultado inteiro da divisao
        r = a % b  # calcula o resto da divisao
        a = b
        b = r

    # while b != 0:
    #    a, b = b, a % b

    return a


def xgcd(a: int, b: int) -> list:

    if b == 0:
        return [1, 0, a]
    else:
        x, y, d = xgcd(b, a % b)

    return [y, x - (a // b) * y, d]


# Find the multiplicative inverse of x (mod y)
# see: http://en.wikipedia.org/wiki/Modular_multiplicative_inverse
def find_inverse(a: int, b: int):
    inv = xgcd(a, b)[0]
    if inv < 1:
        inv += b  # Nós queremos apenas números positivos
    return inv
