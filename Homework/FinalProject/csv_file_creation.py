import csv
from datetime import datetime

# def csv_file_creation(input_list):
#     try:
#         if not input_list:
#             raise ValueError("The input list is empty.")

    
#         current_datetime = datetime.now()
#         filename = f"data_{current_datetime.strftime('%Y-%m-%d_%H-%M-%S')}.csv"

#         with open(filename, 'w', newline='', encoding='utf-8') as file:
#             writer = csv.writer(file)
#             writer.writerow(['Elements'])
#             for element in input_list:
#                 writer.writerow([element])

#         print(f"CSV file '{filename}' created successfully.")
#     except ValueError as e:
#         print(e)
#     except Exception as e:
#         print(f"An error occurred: {e}")


# my_list = ['ciocolata', 'biscuiti', 'napolitane', 'snacks']
# csv_file_creation(my_list)

# empty_list = []
# csv_file_creation(empty_list)

def csv_file_creation(input_dict):
    try:
        if not input_dict:
            raise ValueError("The SubCategory not found.")
        
        current_datetime = datetime.now()
        filename = f"data_{current_datetime.strftime('%Y-%m-%d_%H-%M-%S')}.csv"

        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
        
            writer.writerow(input_dict.keys())
            
            num_rows = max(len(v) for v in input_dict.values())
            for i in range(num_rows):
                row_data = [input_dict[key][i] if i < len(input_dict[key]) else '' for key in input_dict.keys()]
                writer.writerow(row_data)

        print(f"CSV file '{filename}' created successfully.")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"Fatality: {e}")

my_dict = {
    'Product': ['ciocolata', 'biscuiti', 'napolitane', 'snacks'],
    'SubCategory': ['alba', 'crema', 'vanilie', 'chipsuri']
}
csv_file_creation(my_dict)

empty_dict = {}
csv_file_creation(empty_dict)




