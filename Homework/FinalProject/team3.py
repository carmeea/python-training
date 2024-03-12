import csv
import sys

file_path = "/home/denisa/work/python-training/Homework/FinalProject/data.csv"
output_path = "/home/denisa/work/python-training/Homework/FinalProject"


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
    sorted_items = sorted(items)
    print("Available Subcategories:")
    for i, item in enumerate(sorted_items, start=1):
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


def filter_products_by_subcategory(file_path, selected_subcategory):
    try:
        with open(file_path, "r") as file:
            #read the csv and create a list with all the products that are matching the subcategory given by the user
            csv_reader = csv.reader(file)
            #skip the first row (header)
            next(csv_reader) 
            #match between the user's input and what is in the first csv after the url's 4th slash
            #by using lower we convert the subcategory given by the user and the one from the csv so the comparison is case-insensitive
            products = [row for row in csv_reader if selected_subcategory.lower() == row[1].split("/")[4].replace("-", " ").lower()]
            return products
    except FileNotFoundError:
        print(f"File {file_path} not found. Aborting")
        sys.exit(1)
    except OSError:
        print(f"OS error occurred trying to open {file_path}")
        sys.exit(1)
    except Exception as err:
        print(f"Unexpected error opening {file_path} is", repr(err))
        sys.exit(1)


def write_to_csv(products, selected_subcategory):
    try:
        #open the first CSV file to read the header
        with open(file_path, "r") as file:
            csv_reader = csv.reader(file)
            #read the header row
            header = next(csv_reader)
            #replaced the key with Product name
            header[0] = "Product name"
        #open a new csv file for writing the products which will have the name as: subcategoryname_producs.csv
        #replace spaces with underscores in the subcategory name   
        file_name = selected_subcategory.replace(" ", "_")
        #set the path for the csv creation
        with open(f"{output_path}/{file_name}_products.csv", "w", newline='') as file:
            csv_writer = csv.writer(file)
            #write the header row and the products
            csv_writer.writerow(header)
            csv_writer.writerows(products)
        print(f"Products matching subcategory '{selected_subcategory}' have been written to '{selected_subcategory}_products.csv'")
    except Exception as err:
        print("Error occurred while writing to CSV:", repr(err))

subcategories = extract_unique_subcategory_from_file(file_path)
display_subcategories(subcategories)
selected_subcategory = get_user_subcategory(subcategories)
print(f"\nYou selected: {selected_subcategory}")

filtered_products = filter_products_by_subcategory(file_path, selected_subcategory)
write_to_csv(filtered_products, selected_subcategory)