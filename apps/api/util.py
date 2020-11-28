from datetime import datetime


def get_year_and_quarter():
    now = datetime.now()

    year = now.year
    month = now.month

    if 1 <= month < 3:
        quarter = 3
    elif 3 <= month < 6:
        quarter = 1
    elif 6 <= month < 9:
        quarter = 4
    else:
        quarter = 2

    return year, quarter
