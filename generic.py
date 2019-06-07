import random


def is_prime(number: int) -> bool:
    """
    Test to see if a number is prime.
    """
    if number == 2 or number == 3:
        return True

    if number < 2 or number % 2 == 0:
        return False

    # tenta dividir pelos números a partir de 3 até sua metade, andando de 2 em 2
    for n in range(3, int(number / 2) + 2, 2):
        if (number % n) == 0:
            return False

    return True


def is_prime_fermat(number: int, k=7) -> bool:
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
        if pow(a, number - 1, number) != 1:
            return False
    return True


def is_prime_fermat_2(number: int) -> bool:
    if number == 2:
        return True
    if not number & 1:
        return False
    return pow(2, number - 1, number) == 1


def is_prime_fermat_3(n) -> bool:
    a = random.randint(1, (n - 1))
    while gcd(a, n) != 1:
        a = random.randint(1, (n - 1))
    return pow(a, (n - 1), n) == 1


def is_prime_miller(number: int, k=10) -> bool:
    # https://gist.github.com/bnlucas/5857478
    if number == 2 or number == 3:
        return True
    if not number & 1:
        return False

    def check(a, s, d, number) -> bool:
        x = pow(a, d, number)
        if x == 1:
            return True
        for i in range(s - 1):
            if x == number - 1:
                return True
            x = pow(x, 2, number)
        return x == number - 1

    s = 0
    d = number - 1

    while d % 2 == 0:
        d >>= 1
        s += 1

    for i in range(k):
        a = random.randrange(2, number - 1)
        if not check(a, s, d, number):
            return False
    return True


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
