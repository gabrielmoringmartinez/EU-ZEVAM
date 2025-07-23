# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

import os
import shutil


def ensure_clean_directory(path):
    """
       Deletes all contents of the specified directory and recreates it as an empty directory.

       This is useful to ensure a clean output folder before saving new results,
       avoiding conflicts or mixing with previous data.

       Parameters:
           path (str): The file system path to the directory to be cleaned.

       Returns:
           None
       """
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)
