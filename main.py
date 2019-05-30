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

import rsa
import random

prime_number_limit = 100






def generate_prime():
    # números primos são valores inteiros maiores que 1
    # divisíveis apenas por 1 e por si mesmos

    # gera número aleatorio entre 2 e prime_number_limit
    number = random.randint(2,prime_number_limit)

    # se for par, soma 1 para ser ímpar (pares não são primos, exceto 2)
    if (number % 2) == 0:
        number += 1

    # enquanto não for primo, soma dois e tenta novamente
    while not is_prime(number):
        number += 2
        
    return number



def is_prime(number):
    """
    Test to see if a number is prime.
    """

    is_prime = True 

    # tenta dividir pelos números a partir de 3 até sua metade, andando de 2 em 2
    for n in range(3, int(number/2)+2, 2):
        if (number % n) == 0:
            is_prime = False
            break
        
    return is_prime








q = generate_prime()
p = generate_prime()


n = p * q



    
