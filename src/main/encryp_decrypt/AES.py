from loguru import logger
import base64
import os
import sys

from Cryptodome.Cipher import AES
from Cryptodome.Protocol.KDF import PBKDF2
from dotenv import load_dotenv
from pathlib import Path

# Load .env from explicit path
env_path = Path("/Users/lmno3418/Documents/PROJECTS/project1/src/resources/.env")
load_dotenv(dotenv_path=env_path)

try:
    key = os.getenv("KEY")
    iv = os.getenv("IV")
    salt = os.getenv("SALT")

    if not (key and iv and salt):
        raise Exception("Error while fetching details for key/iv/salt")
except Exception as e:
    logger.error("Error occurred. Details: {}", e)
    sys.exit(1)

BS = 16
pad = lambda s: bytes(s + (BS - len(s) % BS) * chr(BS - len(s) % BS), 'utf-8')
unpad = lambda s: s[0:-ord(s[-1:])]

def get_private_key():
    Salt = salt.encode('utf-8')
    kdf = PBKDF2(key, Salt, 64, 1000)
    return kdf[:32]

def encrypt(raw):
    raw = pad(raw)
    cipher = AES.new(get_private_key(), AES.MODE_CBC, iv.encode('utf-8'))
    return base64.b64encode(cipher.encrypt(raw)).decode('utf-8')

def decrypt(enc):
    cipher = AES.new(get_private_key(), AES.MODE_CBC, iv.encode('utf-8'))
    return unpad(cipher.decrypt(base64.b64decode(enc))).decode('utf-8')


# if __name__ == "__main__":
#     print(encrypt("manish"))
#     print(decrypt("U1AMRIQSTYosVJCmmqUHnA=="))
    
    
#     print(encrypt("root"))                      #AIXahH+g2S6L8V/bAnlxcA==
#     print(encrypt("password"))                  #/3N2Xy/Zr3a7StzU1N6wrg==
#     print(encrypt("home_builder"))              #qI6YK97+xD/VxiNJJp2zhw==
