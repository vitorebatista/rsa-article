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


from rsa_benchmark import rsa_benchmark
from graph import graphPlot

message = "Projeto e Análise de Algoritmos (PAA) - Universidade do Estado de Santa Catarina (UDESC) 2019"
rsa_benchmark(type='fermat', message=message, bits=8)



