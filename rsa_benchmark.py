from rsa import Rsa
import time


def rsa_benchmark(message="Hello World!", bits=24, type="brutal") -> tuple:
    timesEncrypt = []
    timesBrutal = []
    average = 30
    for i in range(1, bits // 2 + 1):
        bit = i * 2
        timeEncrypt = 0
        timeBrutal = 0
        for m in range(1, average):
            print(f"Executando com {bit} bits - Tentativa {m}")

            rsa = Rsa()
            rsa.set_bits(bit)
            rsa.set_prime_method(type)
            p = rsa.generate_prime()
            q = rsa.generate_prime(skip=p)
            rsa.generate_keypair(p, q)

            codeValues, breakValues = [], []

            start = time.time()
            coded_message = rsa.encrypt(rsa.publicKey, message)
            timeEncrypt += time.time() - start

            start = time.time()
            broken_message = rsa.brutalForce(coded_message, rsa.publicKey)
            timeBrutal += time.time() - start

        print("broken_message", broken_message)

        timesEncrypt.append(timeEncrypt / average)
        timesBrutal.append(timeBrutal / average)

    return (timesEncrypt, timesBrutal)

