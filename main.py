"""
Implementar um programa para criptografia e descriptografia de um arquivo usando o algoritmo RSA.
Implementar um algoritmo de força bruta para quebra da chave criptográfica e uma heurística
que permita quebrar chaves um pouco maiores que o algoritmo de força bruta (e.g. Pollard-Rho).

É obrigatória a implementação das seguintes funções:
    - Geração das chaves pública e privadas, principalmente a verificação de primalidade de um número;
    - Algoritmo de Euclides Estendido;
    - Função para criptografar e descriptografar dados de um arquivo;
    - Algoritmo de força bruta para a fatoração da chave pública nos números primos que a geraram;
    - Heurística para fatoração de números primos.

Escrever um relatório técnico de até sete páginas no formato de artigo da SBC, o artigo deve conter:
    - Uma introdução sobre o funcionamento de criptografia de chave pública;
    - Uma descrição da complexidade das funções implementadas;
    - Gráficos com os tempos de execução da geração das chaves e dos dois procedimentos de fatoração para inteiros com n-bits.
"""

import math
from rsa import Rsa
from rsaMath import rsaMath

def brutalForce(coded_message, pk):

    decrypted_message = ''

    p = 1
    q = 1

    e = pk[0]
    n = pk[1]

    nSqrt = math.sqrt(n)
    nControl = 3

    #dado n tenta descobrir p e q
    while nControl <= nSqrt:
        if (n % nControl) == 0:
            p = n//nControl
            q = nControl
            break
        nControl += 2
    
    phi = (p-1)*(q-1)

    euclides_array = rsaMath.xgcd(e,phi)
    d = euclides_array[0]

    for c in coded_message:
        decoded_letter = pow(c,d,n)
        decoded_letter = str(chr(decoded_letter))
        decrypted_message += decoded_letter

    return decrypted_message




rsa = Rsa()
coded_message = rsa.encrypt(rsa.publicKey, 'hello world')
decoded_message = rsa.decrypt(coded_message)

broken_message = brutalForce(coded_message, rsa.publicKey)

print(decoded_message)
print(broken_message)
