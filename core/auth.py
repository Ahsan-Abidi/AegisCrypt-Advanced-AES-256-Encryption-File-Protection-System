import json
import bcrypt
import os

DB_PATH = "database/users.json"

os.makedirs("database", exist_ok=True)

if not os.path.exists(DB_PATH):
    with open(DB_PATH, "w") as file:
        json.dump({}, file)

def register_user(username, password):

    with open(DB_PATH, "r") as file:
        users = json.load(file)

    if username in users:
        return False

    hashed = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    ).decode()

    users[username] = hashed

    with open(DB_PATH, "w") as file:
        json.dump(users, file, indent=4)

    return True

def login_user(username, password):

    with open(DB_PATH, "r") as file:
        users = json.load(file)

    if username not in users:
        return False

    stored_hash = users[username].encode()

    return bcrypt.checkpw(
        password.encode(),
        stored_hash
    )