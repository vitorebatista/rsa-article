from generic import is_prime, is_prime_fermat, is_prime_miller
from time import time as t
import numpy as np

'''
O arquivo test_prime.py tem por objetivo validar o funcionamento dos metodos
de teste de primalidade prime (força bruta), fermat e miller, garantindo fidelidade do resultado alcancado
por meio da comparacao com uma lista de números primos gerada previamente
'''

#https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n
def getPrimeList(n):
    """ Returns a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

def print_diff(a1,a2):
    """ Print not similar elements """
    diff = []
    for i in a1:
        if a2.count(i) == 0:
            diff.append(i)
    for i in a2:
        if a1.count(i) == 0:
            if diff.count(i) == 0:
                diff.append(i)
    return diff


amount_test = 100
p0 = getPrimeList(amount_test)
p1, p2, p3, = [], [], []


start = t()
for i in range(2,amount_test):
    p1.append(i) if is_prime(i) else None
print(" # # Teste do método 'is_prime' para %d números" % amount_test)
print("     Tempo decorrido:", t()-start)
print("     Resultado -> OK") if np.array_equal(p0,p1) else print("     Resultado -> PROBLEMA",print_diff(p0,p1))

start = t()
for i in range(2,amount_test):
    p2.append(i) if is_prime_fermat(i) else None
print(" # # Teste do método 'is_prime_fermat' para %d números" % amount_test)
print("     Tempo decorrido:", t()-start)
print("     Resultado -> OK") if np.array_equal(p0,p2) else print("     Resultado -> PROBLEMA",print_diff(p0,p2))

start = t()
for i in range(2,amount_test):
    p3.append(i) if is_prime_miller(i) else None
print(" # # Teste do método 'is_prime_miller' para %d números" % amount_test)
print("     Tempo decorrido:", t()-start)
print("     Resultado -> OK") if np.array_equal(p0,p3) else print("     Resultado -> PROBLEMA",print_diff(p0,p3))