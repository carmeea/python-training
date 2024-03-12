import csv
import datetime

def add_subcategory_field(data):
    for row in data:
        row['Subcategory'] = row['link'].split("/")[4]
    return data

def find_products_for_subcategory(subcategory, data):
    products = []
    csv_subcategory = ''
    for row in data:
        if subcategory.lower() in row['Subcategory'].lower() and subcategory.lower() != 'si' and subcategory.islower():
            products.append(row)
            csv_subcategory = row['Subcategory'].lower()
    return products, csv_subcategory


def export_to_csv(products, subcategory):
    if products:
        filename = f'{subcategory +" "+ str(datetime.datetime.now())}.csv'
        with open(filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=products[0].keys())
            writer.writeheader()
            writer.writerows(products)
        print(f'File "{filename}" was created successfully.')
    else:
        raise ValueError(f'Subcategory not found.')

def main():
    with open('Homework/FinalProject/data.csv', 'r', newline='') as file:
        reader = csv.DictReader(file)
        data = list(reader)

    try:
        data = add_subcategory_field(data)
        subcategory = input('Enter subcategory: ')
        products, csv_category  = find_products_for_subcategory(subcategory, data)
        export_to_csv(products, csv_category)
    
    except ValueError as e:
        print(e)

main()