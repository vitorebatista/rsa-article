"""
Implementar um programa para criptografia e descriptografia de um arquivo usando o algoritmo RSA.
Implementar um algoritmo de força bruta para quebra da chave criptográfica e uma heurística
que permita quebrar chaves um pouco maiores que o algoritmo de força bruta (e.g. Pollard-Rho).

É obrigatória a implementação das seguintes funções:
    - Geração das chaves pública e privadas,
    - principalmente a verificação de primalidade de um número;
    - Algoritmo de Euclides Estendido;
    - Função para criptografar e descriptografar dados de um arquivo;
    - Algoritmo de força bruta para a fatoração da chave pública nos números primos que a geraram;
    - Heurística para fatoração de números primos.

Escrever um relatório técnico de até sete páginas no formato de artigo da SBC, o artigo deve conter:
    - Uma introdução sobre o funcionamento de criptografia de chave pública;
    - Uma descrição da complexidade das funções implementadas;
    - Gráficos com os tempos de execução da geração das chaves e dos dois procedimentos de fatoração para inteiros com n-bits.
"""

from rsa_benchmark import rsa_benchmark
from graph import plot


def measure_encrypt(message, bits_limit):
    """
    Realiza o benchmark do processo de geração de chaves, comparando fermat e miller.
    O resultado desse procedimento é gravado em um arquivo na pasta /time.
    message - mensagem a ser criptografada
    bits_limit - número de bits limite para realizar benchmark
    """
    timesAverage = 10
    fermatEncrypt,[] = rsa_benchmark(message, bits_limit, encryptMethod="fermat", timesAverage=timesAverage)
    millerEncrypt,[] = rsa_benchmark(message, bits_limit, encryptMethod="miller", timesAverage=timesAverage)
    plotEncrypt = {
        "fermat": fermatEncrypt,
        "miller": millerEncrypt
    }

    plot(valuesY=plotEncrypt, title="Encrypt", bits=bits_limit)


def measure_break(message, bits_limit):
    """
    Realiza o benchmark do processo quebra de chaves.
    O resultado desse procedimento é gravado em um arquivo na pasta /time.
    message - mensagem a ser criptografada
    bits_limit - número de bits limite para realizar benchmark
    """
    timesAverage = 1

    pollardBreak = rsa_benchmark(message, bits_limit, breakMethod="pollard", timesAverage=timesAverage)
    pollardBreak = pollardBreak[1]

    bruteBreak = rsa_benchmark(message, bits_limit, breakMethod="brute", timesAverage=timesAverage)
    bruteBreak = bruteBreak[1]

    plotBreak = {
        "pollard": pollardBreak,
        "brute force": bruteBreak
    }

    plot(valuesY=plotBreak, title="Break Key", bits=bits_limit)


# Altere aqui o número de bits desejado
bits_limit = 32
message = "Projeto e Analise de Algoritmos (PAA) - Universidade do Estado de Santa Catarina (UDESC) 2019"

# Chamada da funcão para criptografar
#measure_encrypt(message, bits_limit)

# Chamada da funcão para descriptografar
measure_break(message, bits_limit)