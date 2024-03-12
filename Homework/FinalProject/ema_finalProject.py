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
    with open("Homework/FinalProject/data.csv", "r") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            key = row[0]
            value = tuple(row[1:])
            data_dict[key] = value
    return data_dict


def find_products_by_subcategory(
    data_dict, subcategories, output_file_path, keyword="/Dulciuri-si-snacks/"
):

    keyword = keyword.lower().strip("/")

    for subcategory_input in subcategories:
        found = False  # This flag checks if we found any products for the subcategory.
        output_path = f"{output_file_path}_{subcategory_input}.csv"

        with open(output_path, "w", newline="") as file:
            csv_writer = csv.writer(file)

            csv_writer.writerow(["Key", "URL"])

            for key, value in data_dict.items():
                url = value[0].lower()

                if keyword in url:
                    segments = url.split("/")

                    try:
                        keyword_index = segments.index(keyword)

                        # Check if there's a segment after the keyword, and if it matches the subcategory we're looking for.
                        if (
                            keyword_index + 1 < len(segments)
                            and segments[keyword_index + 1] == subcategory_input
                        ):
                            csv_writer.writerow([key] + list(value))
                            found = True
                    except ValueError:
                        continue

        if not found:
            print(f"Error: Subcategory '{subcategory_input}' not found")
        else:
            print(
                f"Products for subcategory '{subcategory_input}' have been written to '{output_path}'"
            )


subcategories = get_subcategories_input()
data_dict = read_csv("data.csv")
find_products_by_subcategory(data_dict, subcategories, "Homework/FinalProject/")
