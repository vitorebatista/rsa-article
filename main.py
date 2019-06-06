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


from rsa import Rsa
from rsaMath import rsaMath
from graph import graphPlot
import time







rsa = Rsa()
coded_message = rsa.encrypt(rsa.publicKey, 'hello world')
decoded_message = rsa.decrypt(coded_message)

broken_message = rsa.brutalForce(coded_message, rsa.publicKey)

print(decoded_message)
print(broken_message)


graphPlot = graphPlot()

for i in range(1,4):
    rsa = Rsa()
    #rsa.setBitsSize(8*i)
    
    codeValues = []
    breakValues = []

    start = time.time()
    coded_message = rsa.encrypt(rsa.publicKey, 'people turn the tv on and the brain off')
    codeValues =  ['code', 8*i, time.time()-start] 

    start = time.time()
    broken_message = rsa.brutalForce(coded_message, rsa.publicKey)
    breakValues = ['break', 8*i, time.time()-start]

    graphPlot.addValues(codeValues)
    graphPlot.addValues(breakValues)

graphPlot.plot()


