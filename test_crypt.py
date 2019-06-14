from rsa import Rsa
from time import time as t

'''
O arquivo test_crypt.py criptografa uma mensagem de n bits e a descriptografa conhecendo
tanto a chave pública quanto a chave privada
'''

def crypt_test():

    start = t()
    
    rsa = Rsa()
    rsa.set_bits(512) #define o tamanho de p e q
    rsa.set_EncryptMethod('fermat') #define o método para teste de primalidade miller ou fermat
    p = rsa.generate_prime()
    q = rsa.generate_prime(limit=p) 
    rsa.generate_keypair(p, q)

    coded_message = rsa.encrypt(rsa.publicKey, "Felipe Nathan Welter e Vitor Emanuel Batista")
    decoded_message = rsa.decrypt(coded_message)
    #broken_message = rsa.breakMessage(coded_message, rsa.publicKey)

    print(" # # Criptografia com teste de primalidade %s para %d bits" % (rsa.encryptMethod, rsa.bits) )
    print(" # # coded_message:", coded_message)
    print(" # # decoded_message:", decoded_message)
    print(" # # Tempo decorrido: ", t()-start)
    #print("broken_message", broken_message)


crypt_test()