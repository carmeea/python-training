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

            for key in input_dict.keys():
                values_list = list(input_dict[key])  # Convert tuple to list
                writer.writerow([key] + values_list)


        print(f"CSV file '{filename}' created successfully.")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"Fatality: {e}")

# my_dict = {
#     'Product': ['ciocolata', 'biscuiti', 'napolitane', 'snacks'],
#     'SubCategory': ['alba', 'crema', 'vanilie', 'chipsuri']
# }
# csv_file_creation(my_dict)

# empty_dict = {}
# csv_file_creation(empty_dict)




