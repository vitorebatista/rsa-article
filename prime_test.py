from generic import is_prime, is_prime_fermat, is_prime_fermat_2, is_prime_fermat_3, is_prime_miller
from time import time as t
import numpy as np

def getPrimeList(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

def print_diff(a1,a2):
    diff = []
    for i in a1:
        if a2.count(i) == 0:
            diff.append(i)
    for i in a2:
        if a1.count(i) == 0:
            if diff.count(i) == 0:
                diff.append(i)
    return diff

amout_test = 10000
p0 = getPrimeList(amout_test)
p1, p2, p3, p4, p5 = [], [], [] ,[] ,[]

start = t()
for i in range(2,amout_test):
    p1.append(i) if is_prime(i) else None
print("is_prime", t()-start) # is_prime 0.5039529800415039
print("-> OK") if np.array_equal(p0,p1) else print("-> Problema",print_diff(p0,p1))


start = t()
for i in range(2,amout_test):
    p2.append(i) if is_prime_fermat(i) else None
print("is_prime_fermat", t()-start) # is_prime_fermat 7.852689981460571
print("-> OK") if np.array_equal(p0,p2) else print("-> Problema",print_diff(p0,p2))


start = t()
for i in range(2,amout_test):
    p3.append(i) if is_prime_fermat_2(i) else None
print("is_prime_fermat_2", t()-start) # is_prime_fermat_2 0.012823820114135742
print("-> OK") if np.array_equal(p0,p3) else print("-> Problema",print_diff(p0,p3))


start = t()
for i in range(2,amout_test):
    p4.append(i) if is_prime_fermat_3(i) else None
print("is_prime_fermat_3", t()-start) # is_prime_fermat_3
print("-> OK") if np.array_equal(p0,p4) else print("-> Problema",print_diff(p0,p4))


start = t()
for i in range(2,amout_test):
    p5.append(i) if is_prime_miller(i) else None
print("is_prime_miller", t()-start) # is_prime_miller 0.15883302688598633
print("-> OK") if np.array_equal(p0,p5) else print("-> Problema",print_diff(p0,p5))


