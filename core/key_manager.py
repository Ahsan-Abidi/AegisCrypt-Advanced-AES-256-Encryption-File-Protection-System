from Crypto.Protocol.KDF import PBKDF2

KEY_LENGTH = 32

def generate_key(password, salt):

    key = PBKDF2(
        password=password,
        salt=salt,
        dkLen=KEY_LENGTH,
        count=100000
    )

    return key