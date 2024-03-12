import csv


def get_subcategories_input():
    num_subcategories = int(input("How many subcategories do you want to enter? "))
    subcategories = []
    for row in range(num_subcategories):
        subcategory = input("Enter a subcategory: ").strip().lower()
        subcategories.append(subcategory)
    return subcategories


def read_csv(file_path):
    data_dict = {}
    with open(file_path, "r", encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            key = row[0]  # First item in the row is the key.
            value = tuple(row[1:])  # The rest of the items form the value.
            data_dict[key] = value
    return data_dict


# Function to find products related to the subcategories and write them to file
def find_products_by_subcategory(
    data_dict, subcategories, output_file_path, keyword="/Dulciuri-si-snacks/"
):
    keyword = keyword.lower().strip("/")

    for subcategory_input in subcategories:
        matching_products = []  # List to store products matching the subcategory.

        # Loop through each product in our data dictionary.
        for key, value in data_dict.items():
            url = value[
                0
            ].lower()  # Make URL lowercase for case-insensitive comparison.
            if keyword in url:  # Check if our keyword is in the URL.
                segments = url.split("/")  # Split the URL into segments.
                try:
                    subcategory_segment = (
                        segments[4].replace("-", " ").casefold()
                    )  # Process the fifth segment.
                    # Check if our processed segment includes the user's subcategory input.
                    if subcategory_input in subcategory_segment:
                        matching_products.append(
                            (key, segments[4])
                        )  # Add to our list if it's a match.
                except (ValueError, IndexError):
                    # If there's a problem (e.g., the URL doesn't have enough segments), skip this product.
                    continue

        # Only create a file if we found matching products.
        if matching_products:
            output_path = f"{output_file_path}_{subcategory_input}.csv"  # Set the output file path.
            # Open the output file for writing.
            with open(output_path, "w", newline="", encoding="utf-8") as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow(["Key", "URL Segment"])  # Write the header row.
                # Write each matching product to the file.
                for product in matching_products:
                    csv_writer.writerow(product)
            print(
                f"Products for subcategory '{subcategory_input}' have been written to '{output_path}'"
            )
        else:
            # If no products were found, inform the user.
            print(f"Error: Subcategory '{subcategory_input}' not found")


subcategories = get_subcategories_input()  # Get subcategories from user.
data_dict = read_csv("Homework/FinalProject/data.csv")
find_products_by_subcategory(data_dict, subcategories, "Homework/FinalProject/output")
