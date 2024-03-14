import csv
from csv_operations import CsvOperations


class FinalProject:
    @staticmethod
    def project():
        try:
            with open('Homework/FinalProject/data.csv', 'r', newline='') as file:
                reader = csv.DictReader(file)
                data = list(reader)
            subcategory = input('subcategory: ')
            if len(subcategory) <= 4:
                raise Exception("This word is not long enough, no subcategory was found")
            CsvOperations().export_shopping_list(subcategory, data)

        except FileNotFoundError as e:
            print(e, " -> please make sure the file exists and is accessible")


if __name__ == "__main__":
    FinalProject.project()