import os
from datetime import datetime

def get_file_metadata(file_path):

    stats = os.stat(file_path)

    metadata = {
        "File Name": os.path.basename(file_path),
        "Size (KB)": round(stats.st_size / 1024, 2),
        "Created": datetime.fromtimestamp(stats.st_ctime),
        "Modified": datetime.fromtimestamp(stats.st_mtime)
    }

    return metadata