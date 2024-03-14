
import csv
import os


class CsvOperations:
    @staticmethod
    def find_products_from_subcategory(desired_subcategory, data):
        available_products = []
        subcategory_list = []
        for product in data:
            subcategory = product["link"].split("/")[4].lower()
            if subcategory not in subcategory_list:
                subcategory_list.append(subcategory)
            if desired_subcategory.lower() in subcategory and desired_subcategory.lower():
                available_products.append(product)
        return available_products, subcategory_list

    def export_shopping_list(self, desired_items, data):
        shopping_list, subcategory_list = self.find_products_from_subcategory(desired_items, data)
        if shopping_list:
            for i in subcategory_list:
                if desired_items.lower() in i:
                    print(f'File "{i}" was created successfully.')

                    filename = f"{i}.csv" 

                    if os.path.isfile(filename):
                        os.remove(filename)

                    with open(filename, 'w', newline='') as f:
                        writer = csv.DictWriter(f, fieldnames=shopping_list[0].keys())
                        writer.writeheader()
                        writer.writerows(shopping_list)

        else:
            raise ValueError(f"Oh no, the product {desired_items} doesn't exist, your shopping list is empty and the "
                             f"file was not created >.<")
