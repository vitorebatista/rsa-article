import random


def is_prime(number: int) -> bool:
    """
    Test to see if a number is prime.
    """

    is_prime = True

    # tenta dividir pelos números a partir de 3 até sua metade, andando de 2 em 2
    for n in range(3, int(number / 2) + 2, 2):
        if (number % n) == 0:
            is_prime = False
            break

    return is_prime

def is_prime_fermat(n, k = 7) -> bool:
    # https://gist.github.com/Ayrx/5884802
    # Implementation uses the Fermat Primality Test
    
    # If number is even, it's a composite number

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in range(k):
        a = random.randint(1, n-1)

        if pow(a, n-1) % n != 1:
            return False
    return True


def is_prime_fermat_2(n) -> bool:
	if n == 2:
		return True
	if not n & 1:
		return False
	return pow(2, n-1, n) == 1

def is_prime_miller(n, k=10) -> bool:
    #https://gist.github.com/bnlucas/5857478
	if n == 2 or n == 3:
		return True
	if not n & 1:
		return False

	def check(a, s, d, n):
		x = pow(a, d, n)
		if x == 1:
			return True
		for i in range(s - 1):
			if x == n - 1:
				return True
			x = pow(x, 2, n)
		return x == n - 1

	s = 0
	d = n - 1

	while d % 2 == 0:
		d >>= 1
		s += 1

	for i in range(k):
		a = random.randrange(2, n - 1)
		if not check(a, s, d, n):
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
