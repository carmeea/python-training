"""
1. Print your current working directory
"""

from pathlib import Path


def current_working_directory():
    working_directory = Path.cwd()
    print("Current working directory is:", working_directory)
    print("Data type is:", type(working_directory))


current_working_directory()
