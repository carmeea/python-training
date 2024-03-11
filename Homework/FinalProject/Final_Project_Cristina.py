import csv


def find_subcat(subcategory):
    rows = []
    with open("data.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if subcategory.lower() in row[1].lower():
                rows.append(row[0])

    return rows


def write_to_file(subcategory, products):
    filename = f"{subcategory}_Cristina.csv"
    with open(filename, "w", newline="") as file:
        # writer = csv.writer(file)
        for p in products:
            file.write(p + "\n")
    return filename


def main():
    subcategory = input("Enter subcategory: ")
    products = find_subcat(subcategory)
    if products:
        filename = write_to_file(subcategory, products)
        print(f"File {filename} was created")
    else:
        print("Subcategory not found")


if __name__ == "__main__":
    main()
