import base64


def save_public_key(bits, key):
    # Salva a chave púplica em um arquivo
    fileName = f"./files/{bits}_encrypt"
    encryptFile = open(f"{fileName}.pem", "w+")
    encryptFile.seek(0), encryptFile.truncate()
    encryptFile.write(f"-----BEGIN PUBLIC KEY-----\n")
    unencoded = ",".join(map(str, key))
    encoded = base64.b64encode(unencoded.encode())
    encryptFile.write(encoded.decode())
    encryptFile.write("\n-----END PUBLIC KEY-----")
    encryptFile.close()


def save_message(bits, message):
    fileName = f"./files/{bits}_encrypt"
    encryptFile = open(f"{fileName}.msg", "w+")
    encryptFile.seek(0), encryptFile.truncate()
    unencoded = ",".join(map(str, message))
    encoded = base64.b64encode(unencoded.encode())
    encryptFile.write(encoded.decode())
    encryptFile.close()


def read_public_key(bits) -> list:
    fileName = f"./files/{bits}_encrypt.pem"
    encryptFile = open(fileName, "r")
    encryptFile.readline()
    line = encryptFile.readline()
    # publicKey=publicKey.replace('\n', '')
    lineDecode = base64.b64decode(line.encode())
    publicKey = list(map(int, lineDecode.decode().split(",")))
    encryptFile.close()
    return publicKey

def read_message(bits) -> list:
    fileName = f"./files/{bits}_encrypt.msg"
    encryptFile = open(fileName, "r")
    line = encryptFile.readline()
    # publicKey=publicKey.replace('\n', '')
    lineDecode = base64.b64decode(line.encode())
    message = list(map(int, lineDecode.decode().split(",")))
    encryptFile.close()
    return message
