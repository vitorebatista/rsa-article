from rsa import Rsa
from files import read_message, read_public_key

bit = 12
# Faz a leitura do arquivo de chave .pem
publicKey = read_public_key(bit)

# Faz a leitura do arquivo da mensagem .msg
coded_message = read_message(bit)
rsa = Rsa()
broken_message = rsa.brutalForce(coded_message, publicKey)

print("Quebra do arquivo criptografado para chave de %n bits" & bit)
print(broken_message)
