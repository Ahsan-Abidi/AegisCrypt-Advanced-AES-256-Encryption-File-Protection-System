import os

from Crypto.Cipher import AES

from core.key_manager import generate_key
from core.logger import (
    write_activity,
    write_error
)

BLOCK_SIZE = 16

def unpad_data(data):

    padding_length = data[-1]

    return data[:-padding_length]

def decrypt_file(file_path, password):

    try:

        os.makedirs(
            "decrypted_files",
            exist_ok=True
        )

        with open(file_path, "rb") as file:

            salt = file.read(16)

            iv = file.read(16)

            encrypted_data = file.read()

        key = generate_key(
            password,
            salt
        )

        cipher = AES.new(
            key,
            AES.MODE_CBC,
            iv
        )

        decrypted_padded = cipher.decrypt(
            encrypted_data
        )

        decrypted_data = unpad_data(
            decrypted_padded
        )

        original_filename = (
            os.path.basename(file_path)
            .replace(".enc", "")
        )

        output_path = os.path.join(
            "decrypted_files",
            f"decrypted_{original_filename}"
        )

        with open(output_path, "wb") as file:
            file.write(decrypted_data)

        write_activity(
            f"Decrypted File: {file_path}"
        )

        return output_path

    except Exception as error:

        write_error(
            f"Decryption Error: {str(error)}"
        )

        return None