"""
8. Converts a number of seconds to a date
"""

from datetime import datetime


def convert_seconds_date(seconds):
    print(datetime.fromtimestamp(seconds).strftime("%A, %B %d, %Y %I:%M:%S"))


convert_seconds_date(9472583697)
