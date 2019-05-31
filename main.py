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

rsa = Rsa()

# 1. selecione ao acaso dois números primos grandes p e q, tal qu p <> q.
# os primos p e q podem ter, digamos, 512 bits cada um

q = rsa.generate_prime()
p = rsa.generate_prime()

# garante que sejam números diferentes
while (p == q):
    q = rsa.generate_prime()

# 2. calcule n pela equacao n = p*q
n = p * q

# 3. selecione um inteiro ímpar pequeno 'e' tal que ele seja primo em relacao
# a phi(n) que, pela equacao é igual a (p-1)*(q-1)
phi = (p-1)*(q-1)
e = rsa.generate_prime(phi)

while ( rsa.gcd(e,phi) != 1 ):
    e = rsa.generate_prime(phi)




letra = ord('a')
print( "ascii %d é %s " % (letra, str(chr(letra)) )  )

