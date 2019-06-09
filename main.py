"""
Implementar um programa para criptografia e descriptografia de um arquivo usando o algoritmo RSA.
Implementar um algoritmo de força bruta para quebra da chave criptográfica e uma heurística
que permita quebrar chaves um pouco maiores que o algoritmo de força bruta (e.g. Pollard-Rho).

É obrigatória a implementação das seguintes funções:
    - [ok] Geração das chaves pública e privadas,
    - [ok] principalmente a verificação de primalidade de um número;
    - [ok] Algoritmo de Euclides Estendido;
    - [ok] Função para criptografar e descriptografar dados de um arquivo;
    - [ok] Algoritmo de força bruta para a fatoração da chave pública nos números primos que a geraram;
    - [ok] Heurística para fatoração de números primos.

Escrever um relatório técnico de até sete páginas no formato de artigo da SBC, o artigo deve conter:
    - Uma introdução sobre o funcionamento de criptografia de chave pública;
    - Uma descrição da complexidade das funções implementadas;
    - Gráficos com os tempos de execução da geração das chaves e dos dois procedimentos de fatoração para inteiros com n-bits.
"""


from rsa_benchmark import rsa_benchmark
from graph import plot

bits=24
message = "Projeto e Análise de Algoritmos (PAA) - Universidade do Estado de Santa Catarina (UDESC) 2019"
brutalEncrypt, brutalBrutal = rsa_benchmark(message, bits, type="brutal",)
fermatEncrypt, fermatBrutal = rsa_benchmark(message, bits, type="fermat")
millerEncrypt, millerBrutal = rsa_benchmark(message, bits, type="miller")
plotBrutal = {
    "brutal": brutalBrutal,
    "fermat": fermatBrutal,
    "miller": millerBrutal,
}
plotEncrypt = {
    "brutal": brutalEncrypt,
    "fermat": fermatEncrypt,
    "miller": millerEncrypt,
}

plot(values=plotBrutal, title="Brute Force", bits=bits)
plot(values=plotEncrypt, title="Encrypt", bits=bits)

