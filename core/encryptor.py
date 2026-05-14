import os

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

from core.key_manager import generate_key
from core.logger import (
    write_activity,
    write_error
)

BLOCK_SIZE = 16

def pad_data(data):

    padding_length = BLOCK_SIZE - (
        len(data) % BLOCK_SIZE
    )

    padding = bytes(
        [padding_length]
    ) * padding_length

    return data + padding

def encrypt_file(file_path, password):

    try:

        os.makedirs(
            "encrypted_files",
            exist_ok=True
        )

        with open(file_path, "rb") as file:
            data = file.read()

        salt = get_random_bytes(16)

        key = generate_key(
            password,
            salt
        )

        cipher = AES.new(
            key,
            AES.MODE_CBC
        )

        padded_data = pad_data(data)

        encrypted_data = cipher.encrypt(
            padded_data
        )

        output_filename = (
            os.path.basename(file_path)
            + ".enc"
        )

        output_path = os.path.join(
            "encrypted_files",
            output_filename
        )

        with open(output_path, "wb") as file:

            file.write(salt)

            file.write(cipher.iv)

            file.write(encrypted_data)

        write_activity(
            f"Encrypted File: {file_path}"
        )

        return output_path

    except Exception as error:

        write_error(
            f"Encryption Error: {str(error)}"
        )

        return None