from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from base64 import b64encode
from Crypto.Cipher import AES

def getusername_paswd():
    username = input("Enter your username: ")
    password = input("Enter your password: "
                     "\n 1. Must be 8 characters or more,"
                     "\n 2. Contains at least one Capital letter,"
                     "\n 3. Contains at least one lowercase letter,"
                     "\n 4. Contains at least one number,"
                     "\n 5. and has at least one {#,@,%,*}")