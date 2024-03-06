"""
4. Return path of a specific file
"""

import os
from pathlib import Path


def find_path1():
    # Find the directory we executed the script from:
    execution_dir = os.getcwd()

    # Find the directory in which the current script resides:
    file_dir = os.path.dirname(os.path.realpath(__file__))

    absolute_path = Path(__file__).parent.absolute()

    print(f"Execution dir: {execution_dir}")
    print(f"File dir: {file_dir}")
    print(f"Absolute path: {absolute_path}")


def find_path2():
    directory = (
        "/home/elena/Desktop/PythonWork/python-training/Homework/FunctionsAndModules"
    )
    file = "factorial.py"
    path = os.path.join(directory, file)
    print("Find path:", path)


find_path1()
find_path2()
