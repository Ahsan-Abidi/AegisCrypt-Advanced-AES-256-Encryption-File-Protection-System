import os
from datetime import datetime

LOG_DIR = "logs"

ACTIVITY_LOG = os.path.join(
    LOG_DIR,
    "activity_logs.txt"
)

SECURITY_LOG = os.path.join(
    LOG_DIR,
    "security_logs.txt"
)

ERROR_LOG = os.path.join(
    LOG_DIR,
    "error_logs.txt"
)

os.makedirs(LOG_DIR, exist_ok=True)

def write_activity(message):

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    with open(ACTIVITY_LOG, "a") as file:
        file.write(
            f"[{timestamp}] {message}\n"
        )

def write_security(message):

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    with open(SECURITY_LOG, "a") as file:
        file.write(
            f"[{timestamp}] {message}\n"
        )

def write_error(message):

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    with open(ERROR_LOG, "a") as file:
        file.write(
            f"[{timestamp}] {message}\n"
        )