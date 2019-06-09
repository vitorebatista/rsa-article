import time
from rsa import Rsa
from files import read_public_key, read_message, save_message, save_public_key


def rsa_benchmark(message: str ="Hello World!", bits=24, type="brutal") -> tuple:
    timesEncrypt = []
    timesBrutal = []
    average = 15
    for i in range(1, bits // 2 + 1):
        bit = i * 2
        timeEncrypt = []
        timeBrutal = []
        
        for m in range(0, average):
            print(f"Executando com {bit} bits - Tentativa {m}")
            start = time.time()

            rsa = Rsa()
            rsa.set_bits(bit)
            rsa.set_prime_method(type)
            p = rsa.generate_prime()
            q = rsa.generate_prime(skip=p)
            rsa.generate_keypair(p, q)

            coded_message = rsa.encrypt(rsa.publicKey, message)
            timeEncrypt.append(time.time() - start)
            
            # Salva a chave púplica em um arquivo .pem
            save_public_key(bit, rsa.publicKey)
            
            # Salva a mensagem em um arquivo .msg
            save_message(bit, coded_message)

            # Faz a leitura do arquivo de chave .pem
            publicKey = read_public_key(bit)

            # Faz a leitura do arquivo da mensagem .msg
            coded_message = read_message(bit)

            start = time.time()
            broken_message = rsa.brutalForce(coded_message, publicKey)
            timeBrutal.append(time.time() - start)

        print("broken_message", broken_message)
        # Ordena a lista e remove o primeiro menor item e o último com o maior número
        timeEncrypt.sort()
        del timeEncrypt[0]
        del timeEncrypt[-1]

        timeBrutal.sort()
        del timeBrutal[0]
        del timeBrutal[-1]
        timesEncrypt.append(sum(timeEncrypt) / (average - 2))
        timesBrutal.append(sum(timeBrutal) / (average - 2))

    return (timesEncrypt, timesBrutal)

