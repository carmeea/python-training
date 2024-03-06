"""
1. Print your current working directory
"""

import os


def current_working_directory():
    working_directory = os.getcwd()
    print("Current working directory is:", working_directory)
    print("Data type is:", type(working_directory))


current_working_directory()
