from rsa import Rsa
from files import read_message, read_public_key
bit = 6
# Faz a leitura do arquivo de chave .pem
publicKey = read_public_key(bit)

# Faz a leitura do arquivo da mensagem .msg
coded_message = read_message(bit)
rsa = Rsa()
broken_message = rsa.brutalForce(coded_message, publicKey)
print(broken_message)
