import time
from rsa import Rsa
from files import read_public_key, read_message, save_message, save_public_key

def rsa_benchmark(message: str ="Hello World!", bits_limit: int = 24, encryptMethod: str ="fermat", breakMethod: str ="", timesAverage: int = 10) -> tuple:
    '''
    Função para executar timesAverage vezes os métodos de criptografia para gerar uma média de tempo
    de execução e apresentar um gráfico comparativo. O resultado é salvo num arquivo que
    tem nome no formato <bits>_<encryptMethod>_<breakMethod>.

    message - String com a mensagem a ser criptografada. Default: "Hello World!"
    bits_limit - Número de bits considerado no processo de criptografia. Default: 24
    encryptMethod - Método de análise de número primo (miller ou fermat). Default: fermat
    breakMethod - Método de força bruta (brute ou pollard). Default: brute
    timesAverage - Quantidade de vezes em que deve ser executado para gerar a média de tempo
    '''

    timesEncrypt = []
    timesBreak = []

    encryptFileName = f"./files/time/{bits_limit}_{encryptMethod}_encrypt.time"
    encryptFileName = open(encryptFileName, "w+")
    
    if(breakMethod):
        breakFileName = f"./files/time/{bits_limit}_{encryptMethod}_{breakMethod}.time"
        breakFileName = open(breakFileName, "w+")
        broken_message = ""

    for i in range(1, bits_limit // 8 + 1):
        #comeca com 4 bits pq é o mínimo para phi suportar abela ASCII
        bit = i * 8
        timeEncrypt = []
        timeBreak = []
        average = timesAverage
        
        for m in range(0, timesAverage):
            print(f"Executando com {bit} bits encryptMethod={encryptMethod} breakMethod={breakMethod} - Execucao {m}")
            
            rsa = Rsa()
            rsa.set_bits(bit)
            rsa.set_EncryptMethod(encryptMethod)
            rsa.set_BreakMethod(breakMethod)

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

            # faz a quebra e mede o tempo
            if(breakMethod):
                # Faz a leitura do arquivo de chave .pem
                publicKey = read_public_key(bit)

                # Faz a leitura do arquivo da mensagem .msg
                coded_message = read_message(bit)

                start = time.time()
            
                broken_message = rsa.breakMessage(coded_message, publicKey)
                timeBreak.append(time.time() - start)

                print(f"{bit} bits - broken_message", broken_message)

        # Ordena a lista e remove o primeiro menor item e o último com o maior número
        if(timesAverage > 2):
            average = (timesAverage - 2)
            timeEncrypt.sort()
            del timeEncrypt[0]
            del timeEncrypt[-1]
            if(breakMethod):
                timeBreak.sort()
                del timeBreak[0]
                del timeBreak[-1]

        # calcula média (encrypt) das timesAverage execucoes
        timesEncrypt.append(sum(timeEncrypt) / average)
        encryptFileName.write(f"{bit}\t{sum(timeEncrypt) / average}\n")
        
        # calcula média (break) das timesAverage execucoes
        if(breakMethod):
            timesBreak.append(sum(timeBreak) / average)
            breakFileName.write(f"{bit}\t{sum(timeBreak) / average}\n")
    
    # Fecha arquivos abertos
    encryptFileName.close()
    if(breakMethod):
        breakFileName.close()

    return (timesEncrypt, timesBreak)

