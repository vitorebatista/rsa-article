import base64


def save_public_key(bits: int, key: list):
    # Salva a chave pública em um arquivo .pem na pasta files
    fileName = f"./files/{bits}_encrypt"
    encryptFile = open(f"{fileName}.pem", "w+")
    encryptFile.seek(0), encryptFile.truncate()
    encryptFile.write(f"-----BEGIN PUBLIC KEY-----\n")
    unencoded = ",".join(map(str, key))
    encoded = base64.b64encode(unencoded.encode())
    encryptFile.write(encoded.decode())
    encryptFile.write("\n-----END PUBLIC KEY-----")
    encryptFile.close()


def save_message(bits: int, message):
    # Salva a mensagem em um arquivo .msg na pasta files
    fileName = f"./files/{bits}_encrypt"
    encryptFile = open(f"{fileName}.msg", "w+")
    encryptFile.seek(0), encryptFile.truncate()
    unencoded = ",".join(map(str, message))
    encoded = base64.b64encode(unencoded.encode())
    encryptFile.write(encoded.decode())
    encryptFile.close()


def read_public_key(bits: int) -> list:
    # Le arquivo .pem e converte para o padrão da classe RSA
    fileName = f"./files/{bits}_encrypt.pem"
    encryptFile = open(fileName, "r")
    encryptFile.readline()
    line = encryptFile.readline()
    # publicKey=publicKey.replace('\n', '')
    lineDecode = base64.b64decode(line.encode())
    publicKey = list(map(int, lineDecode.decode().split(",")))
    encryptFile.close()
    return publicKey

def read_message(bits: int) -> list:
    # Le o arquivo .msg e converte para o padrão da classe RSA
    fileName = f"./files/{bits}_encrypt.msg"
    encryptFile = open(fileName, "r")
    line = encryptFile.readline()
    # publicKey=publicKey.replace('\n', '')
    lineDecode = base64.b64decode(line.encode())
    message = list(map(int, lineDecode.decode().split(",")))
    encryptFile.close()
    return message
