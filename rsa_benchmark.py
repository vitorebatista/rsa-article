import time
from rsa import Rsa
from files import read_public_key, read_message, save_message, save_public_key

def rsa_benchmark(message: str ="Hello World!", bits_limit: int = 24, type: str ="prime", method: str ="brute", timesAverage: int = 10) -> tuple:
    '''
    Função para executar 15x os métodos de criptografia para gerar uma média de tempo
    de execução e apresentar um gráfico comparativo.

    message - String com a mensagem a ser criptografada. Default: "Hello World!"
    bits_limit - Número de bits considerado no processo de criptografia. Default: 24
    type - Método de análise de número primo (prime, miller ou fermat). Default: prime
    method - Método de força bruta (brute ou pollard). Default: brute
    timesAverage - Quantidade de vezes em que deve ser executado para gerar a média de tempo
    '''
    timesEncrypt = []
    timesBreak = []
    breakFileName = f"./files/{bits_limit}_{type}_{method}.time"
    breakFileName = open(breakFileName, "w+")
    encryptFileName = f"./files/{bits_limit}_{type}_encrypt.time"
    encryptFileName = open(encryptFileName, "w+")
    for i in range(2, bits_limit // 2 + 1):
        #comeca com 4 bits pq é o mínimo para phi suportar abela ASCII
        bit = i * 2 #tamanho máximo (multiplica n bits por n bits)
        timeEncrypt = []
        timeBreak = []
        average = timesAverage
        for m in range(0, timesAverage):
            print(f"Executando com {bit} bits type={type} method={method} - Tentativa {m}")
            
            rsa = Rsa()
            rsa.set_bits(bit)
            rsa.set_prime_method(type)
            rsa.set_force_brute_method(method)

            start = time.time()
            p = rsa.generate_prime()
            q = rsa.generate_prime(ignore=p)
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
            timeBreak.append(time.time() - start)
            print(time.time() - start)

        print(f"{bit} bits - broken_message", broken_message)
        if(timesAverage > 2):
            average = (timesAverage - 2)
            # Ordena a lista e remove o primeiro menor item e o último com o maior número
            timeEncrypt.sort()
            del timeEncrypt[0]
            del timeEncrypt[-1]

            timeBreak.sort()
            del timeBreak[0]
            del timeBreak[-1]
        timesEncrypt.append(sum(timeEncrypt) / average)
        timesBreak.append(sum(timeBreak) / average)
        breakFileName.write(f"{bit}\t{sum(timeBreak) / average}\n")
        encryptFileName.write(f"{bit}\t{sum(timeEncrypt) / average}\n")
    breakFileName.close()
    encryptFileName.close()

    return (timesEncrypt, timesBreak)

