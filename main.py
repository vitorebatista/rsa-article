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

bits_limit=16
message = "Projeto e Analise de Algoritmos (PAA) - Universidade do Estado de Santa Catarina (UDESC) 2019"
brutalEncrypt, brutalBreak, bitSizes = rsa_benchmark(message, bits_limit, type="brutal",)
fermatEncrypt, fermatBreak, bitSizes = rsa_benchmark(message, bits_limit, type="fermat")
millerEncrypt, millerBreak, bitSizes = rsa_benchmark(message, bits_limit, type="miller")
plotBreak = {
    "brutal": brutalBreak,
    "fermat": fermatBreak,
    "miller": millerBreak,
}
plotEncrypt = {
    "brutal": brutalEncrypt,
    "fermat": fermatEncrypt,
    "miller": millerEncrypt,
}

plot(valuesY=plotBreak, valuesX=bitSizes, title="Brute Force", bits=bits_limit)
plot(valuesY=plotEncrypt, valuesX=bitSizes, title="Encrypt", bits=bits_limit)

