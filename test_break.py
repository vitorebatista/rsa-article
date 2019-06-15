from rsa import Rsa
from files import read_message, read_public_key
from time import time as t

'''
O arquivo test_break.py abre uma chave pública previamente salva e uma mensagem criptografada
previamente salva, realiza a quebra da chave e imprime em tela
'''

#define qual arquivo deve abrir no formato "/XX_encrypt.pem" e "/XX_encrypt.msg"
bit = 64

# Faz a leitura do arquivo de chave .pem
publicKey = read_public_key(bit)

# Faz a leitura do arquivo da mensagem .msg
coded_message = read_message(bit)

start = t()

rsa = Rsa()
rsa.set_BreakMethod("pollard") #pollard or brute
broken_message = rsa.breakMessage(coded_message, publicKey)

print(" # # Quebra do arquivo criptografado para chave de %d bits" % bit)
print("     Tempo decorrido: ", t()-start)
print("     Conteúdo: ", broken_message)
