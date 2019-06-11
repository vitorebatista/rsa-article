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

def call_pollard(message, bits_limit):
    """
    Realiza o benchmark utilizando Pollard-Rho para quebra de chave publica.
    message - mensagem a ser criptografada
    bits_limit - número de bits limite para realizar benchmark
    """
    timesAverage = 10
    primeEncrypt, primeBreak = rsa_benchmark(message, bits_limit, type="prime", method="pollard", timesAverage=timesAverage)
    fermatEncrypt, fermatBreak = rsa_benchmark(message, bits_limit, type="fermat", method="pollard", timesAverage=timesAverage)
    millerEncrypt, millerBreak = rsa_benchmark(message, bits_limit, type="miller", method="pollard", timesAverage=timesAverage)
    plotBreak = {
        "prime": primeBreak,
        "fermat": fermatBreak,
        "miller": millerBreak,
    }
    plotEncrypt = {
        "prime": primeEncrypt,
        "fermat": fermatEncrypt,
        "miller": millerEncrypt,
    }

    plot(valuesY=plotBreak, title="Pollard Rho", bits=bits_limit)
    plot(valuesY=plotEncrypt, title="Encrypt", bits=bits_limit)


def call_brute(message, bits_limit):
    """
    Realiza o benchmark utilizando Força Bruta para quebra de chave publica.
    message - mensagem a ser criptografada
    bits_limit - número de bits limite para realizar benchmark
    """
    primeEncrypt, primeBreak = rsa_benchmark(message, bits_limit, type="prime", method="brute")
    fermatEncrypt, fermatBreak = rsa_benchmark(message, bits_limit, type="fermat", method="brute")
    millerEncrypt, millerBreak = rsa_benchmark(message, bits_limit, type="miller", method="brute")
    plotBreak = {
        "prime": primeBreak,
        "fermat": fermatBreak,
        "miller": millerBreak,
    }
    plotEncrypt = {
        "prime": primeEncrypt,
        "fermat": fermatEncrypt,
        "miller": millerEncrypt,
    }

    plot(valuesY=plotBreak, title="Brute Force", bits=bits_limit)
    plot(valuesY=plotEncrypt, title="Encrypt", bits=bits_limit)


bits_limit = 32
message = "Projeto e Analise de Algoritmos (PAA) - Universidade do Estado de Santa Catarina (UDESC) 2019"
call_pollard(message, bits_limit)
call_brute(message, bits_limit)