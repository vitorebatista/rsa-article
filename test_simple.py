
from rsa import Rsa
import time

def simple_test():
    rsa = Rsa()
    # p = rsa.generate_prime()
    # q = rsa.generate_prime(limit=p) # 17

    q = 17
    p = 41
    rsa.set_bits(4)
    rsa.generate_keypair(p, q)
    coded_message = rsa.encrypt(rsa.publicKey, "This is a message 1234 *&6^'/q@1")
    decoded_message = rsa.decrypt(coded_message)
    broken_message = rsa.brutalForce(coded_message, rsa.publicKey)

    print(decoded_message)
    print("broken_message", broken_message)


simple_test()