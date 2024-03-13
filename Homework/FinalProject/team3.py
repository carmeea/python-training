import csv
import sys
import os

file_path = "/home/cosmin/work/python-training/Homework/FinalProject/data.csv"


def extract_unique_subcategory_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            # read csv file and extract the urls (second column) in a list
            csv_reader = csv.reader(file)
            url_lst = [row[1] for row in csv_reader]
            # remove column header which is string "link"
            url_lst.pop(0)
            # split url and replace dashes with spaces from subcategory name
            unique_subcategories = set(url.split("/")[4].replace("-", " ").title() for url in url_lst)
            return list(unique_subcategories)

    except FileNotFoundError:
        print(f"File {file_path} not found. Aborting")
        sys.exit(1)
    except OSError:
        print(f"OS error occurred trying to open {file_path}")
        sys.exit(1)
    except Exception as err:
        print(f"Unexpected error opening {file_path} is", repr(err))
        sys.exit(1)


def display_subcategories(items):
    print("Available Subcategories:")
    for i, item in enumerate(items, start=1):
        print(f"{i}. {item}")


def normalize_input(user_input):
    # ignore dashes and make it title case
    return user_input.replace("-", " ").title()


def get_user_subcategory(subcategories):
    while True:
        user_input = input("Enter the subcategory: ")
        normalized_input = normalize_input(user_input)
        if normalized_input in (normalize_input(sub) for sub in subcategories):
            return normalized_input
        else:
            print("Invalid subcategory. Please enter a valid subcategory.")


def create_csv_for_subcategory(subcategory, input_file_path, output_file_path):
    if os.path.exists(output_file_path):
        print(f"CSV file for '{subcategory}' already exists. Aborting.")
        sys.exit(1)

    with open(input_file_path, "r") as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # Skip the header
        rows_for_subcategory = [row for row in csv_reader if normalize_input(row[1].split("/")[4]) == subcategory]

    with open(output_file_path, "w", newline="") as output_file:
        csv_writer = csv.writer(output_file)
        csv_writer.writerow(header)
        csv_writer.writerows(rows_for_subcategory)
        

subcategories = extract_unique_subcategory_from_file(file_path)
display_subcategories(subcategories)

selected_subcategory = get_user_subcategory(subcategories)

print(f"You selected: {selected_subcategory}")

output_file_path = f"selected_products_{selected_subcategory.replace(' ', '')}.csv"
create_csv_for_subcategory(selected_subcategory, file_path, output_file_path)

print(f"CSV file for '{selected_subcategory}' products created: {output_file_path}")
