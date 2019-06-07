"""
Implementar um programa para criptografia e descriptografia de um arquivo usando o algoritmo RSA.
Implementar um algoritmo de força bruta para quebra da chave criptográfica e uma heurística
que permita quebrar chaves um pouco maiores que o algoritmo de força bruta (e.g. Pollard-Rho).

É obrigatória a implementação das seguintes funções:
    - [ok] Geração das chaves pública e privadas,
    - [ok] principalmente a verificação de primalidade de um número; --fermet
    - [ok] Algoritmo de Euclides Estendido;
    - [pendente] Função para criptografar e descriptografar dados de um arquivo; --Falta o arquivo
    - [ok] Algoritmo de força bruta para a fatoração da chave pública nos números primos que a geraram;
    - [ok] Heurística para fatoração de números primos.

Escrever um relatório técnico de até sete páginas no formato de artigo da SBC, o artigo deve conter:
    - Uma introdução sobre o funcionamento de criptografia de chave pública;
    - Uma descrição da complexidade das funções implementadas;
    - Gráficos com os tempos de execução da geração das chaves e dos dois procedimentos de fatoração para inteiros com n-bits.
"""


from rsa import Rsa
from graph import graphPlot
import time


rsa = Rsa()
# p = rsa.generate_prime()
# q = rsa.generate_prime(limit=p) # 17

q = 17
p = 41
rsa.set_bits(2)
rsa.generate_keypair(p, q)
coded_message = rsa.encrypt(rsa.publicKey, "This is a message 1234 *&6^'/q@1")
decoded_message = rsa.decrypt(coded_message)
broken_message = rsa.brutalForce(coded_message, rsa.publicKey)

print(decoded_message)
print("broken_message", broken_message)


graphPlot = graphPlot()
message = "Projeto e Análise de Algoritmos (PAA) - Universidade do Estado de Santa Catarina (UDESC) 2019"
for i in range(1, 12):
    bits = i * 2
    timeEncrypt = 0
    timeBrutal = 0
    average = 20
    for m in range(1, average):
        print(f"Executando com {bits} bits - Tentativa {m}")

        rsa = Rsa()
        rsa.set_bits(bits)
        rsa.set_prime_method("miller")
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

    graphPlot.addValues(["code", bits, timeEncrypt / average])
    graphPlot.addValues(["break", bits, timeBrutal / average])

graphPlot.plot(rsa.primeMethod)

