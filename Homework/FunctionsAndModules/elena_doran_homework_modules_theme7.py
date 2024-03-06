"""
7. Print current time
"""

from datetime import datetime


def print_current_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current time:", current_time)


print_current_time()
