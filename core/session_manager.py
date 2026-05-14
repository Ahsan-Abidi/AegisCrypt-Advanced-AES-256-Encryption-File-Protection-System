import json
import time

SESSION_FILE = "database/session.json"

def create_session(username):

    session = {
        "username": username,
        "login_time": time.time()
    }

    with open(SESSION_FILE, "w") as file:
        json.dump(session, file)

def clear_session():

    with open(SESSION_FILE, "w") as file:
        json.dump({}, file)