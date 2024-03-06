"""
6. Print current datetime
"""

from datetime import datetime, date


def print_current_date_time():
    now = datetime.now()
    print("Datetime:", now)

    year = now.strftime("%Y")
    print("Year:", year)

    month = now.strftime("%m")
    print("Month:", month)

    day = now.strftime("%d")
    print("Day:", day)

    time = now.strftime("%H:%M:%S")
    print("Time:", time)

    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    print("Date and time:", date_time)


def print_current_date():
    today = date.today()
    print("Today's date:", today)

    today1 = today.strftime("%d/%m/%Y")
    print("Today's date:", today1)

    today2 = today.strftime("%B %d, %Y")
    print("Today's date:", today2)

    today3 = today.strftime("%m/%d/%y")
    print("Today's date:", today3)

    today4 = today.strftime("%b-%d-%Y")
    print("Today's date:", today4)


print_current_date_time()
print_current_date()
