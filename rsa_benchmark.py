from rsa import Rsa
import time


def rsa_benchmark(type="brutal", message="Hello World!", bits=24) -> tuple:
    timesEncrypt = []
    timesBrutal = []
    average = 2
    for i in range(1, bits // 2):
        bits = i * 2
        timeEncrypt = 0
        timeBrutal = 0
        for m in range(1, average):
            print(f"Executando com {bits} bits - Tentativa {m}")

            rsa = Rsa()
            rsa.set_bits(bits)
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

