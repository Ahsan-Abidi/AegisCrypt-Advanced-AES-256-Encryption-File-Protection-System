import os

def secure_delete(file_path):

    if not os.path.exists(file_path):
        return False

    size = os.path.getsize(file_path)

    with open(file_path, "wb") as file:
        file.write(os.urandom(size))

    os.remove(file_path)

    return True