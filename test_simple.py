
from rsa import Rsa
import time

def simple_test():
    rsa = Rsa()
    rsa.set_bits(512)
    rsa.encryptMethod('miller')
    p = rsa.generate_prime()
    q = rsa.generate_prime(limit=p) 
    rsa.generate_keypair(p, q)

    coded_message = rsa.encrypt(rsa.publicKey, "Felipe Nathan Welter e Vitor Emanuel Batista")
    decoded_message = rsa.decrypt(coded_message)
    #broken_message = rsa.breakMessage(coded_message, rsa.publicKey)

    print("coded_message:", coded_message)
    print("decoded_message:", decoded_message)
    #print("broken_message", broken_message)


simple_test()