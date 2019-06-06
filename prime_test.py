from generic import is_prime, is_prime_fermat
from time import time as t

start = t()
for i in range(1,10000):
    is_prime(i)
print("is_prime", t()-start)

start = t()
for i in range(2,10000):
    is_prime_fermat(i)
print("is_prime_fermat", t()-start)

