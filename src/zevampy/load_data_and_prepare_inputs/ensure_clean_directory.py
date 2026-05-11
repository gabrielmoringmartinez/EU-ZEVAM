"""Provide utilities for creating clean output directories."""

# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

import os
import shutil


def ensure_clean_directory(path):
    """
    Delete all contents of a directory and recreate it as an empty directory.

    This is useful to ensure a clean output folder before saving new results,
    avoiding conflicts or mixing with previous data.

    Parameters:
        path (str):
            File system path to the directory to be cleaned.

    Returns:
        None
    """
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)
