from generic import is_prime, is_prime_fermat, is_prime_miller
from time import time as t

start = t()
for i in range(2,10000):
    is_prime(i)
print("is_prime", t()-start) # is_prime 0.5039529800415039

start = t()
for i in range(2,10000):
    is_prime_fermat(i)
print("is_prime_fermat", t()-start) # is_prime_fermat 24.6938419342041

start = t()
for i in range(2,10000):
    is_prime_miller(i)
print("is_prime_miller", t()-start) # is_prime_miller 0.15883302688598633
