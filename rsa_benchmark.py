from rsa import Rsa
import time


def rsa_benchmark(message="Hello World!", bits=24, type="brutal") -> tuple:
    timesEncrypt = []
    timesBrutal = []
    average = 50
    for i in range(1, bits // 2 + 1):
        bit = i * 2
        timeEncrypt = []
        timeBrutal = []
        # encryptFile= open(f"{bits}_encrypt.txt","w+")
        for m in range(0, average):
            print(f"Executando com {bit} bits - Tentativa {m}")
            start = time.time()

            rsa = Rsa()
            rsa.set_bits(bit)
            rsa.set_prime_method(type)
            p = rsa.generate_prime()
            q = rsa.generate_prime(skip=p)
            rsa.generate_keypair(p, q)
            codeValues, breakValues = [], []

            coded_message = rsa.encrypt(rsa.publicKey, message)
            timeEncrypt.append(time.time() - start)
            # encryptFile.write(message)

            start = time.time()
            broken_message = rsa.brutalForce(coded_message, rsa.publicKey)
            timeBrutal.append(time.time() - start)

        print("broken_message", broken_message)
        # Ordena a lista e remove o primeiro menor item e o último com o maior número
        timeEncrypt.sort()
        del timeEncrypt[0]
        del timeEncrypt[-1]

        timeBrutal.sort()
        del timeBrutal[0]
        del timeBrutal[-1]
        average -= 2
        timesEncrypt.append(sum(timeEncrypt) / average)
        timesBrutal.append(sum(timeBrutal) / average)

    return (timesEncrypt, timesBrutal)

