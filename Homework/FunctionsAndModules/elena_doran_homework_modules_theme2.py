"""
2. Create a directory with a file inside it
"""

import os


def create_directory_file():
    try:
        new_directory = "ModulesThemes"
        parent_directory = "/home/elena/Desktop"
        path = os.path.join(parent_directory, new_directory)

        os.mkdir(path)
        print("New directory '% s' created" % new_directory)

        file_path = path + "/Theme2.txt"

        new_file = open(file_path, "w")
        new_file.write("Insert file line")
        new_file.close()

        print(os.path.isfile(file_path))

    except FileNotFoundError:
        print("The file was not found.")
    except FileExistsError:
        print("The file already exists.")
    except Exception as e:
        print(f"An error occurred: {e}")


create_directory_file()
