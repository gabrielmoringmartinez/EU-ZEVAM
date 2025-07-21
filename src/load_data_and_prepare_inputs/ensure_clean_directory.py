import os
import shutil


def ensure_clean_directory(path):
    """Delete all contents of a directory and recreate it."""
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)
