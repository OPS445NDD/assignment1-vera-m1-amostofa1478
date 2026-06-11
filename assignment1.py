#!/usr/bin/env python3
'''
OPS445 Assignment 1
Program: assignment1.py
Author: "Abdul Mostofa"
Semester: "Summer 2026"
The python code in this file (assignment1.py) is original work written by
"Abdul Mostofa". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.
'''
import sys

def day_of_week(year: int, month: int, date: int) -> str:
    "Based on the algorithm by Tomohiko Sakamoto"
    days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + date) % 7
    return days[num]

def leap_year(year: int) -> bool:
    "Return True if the year is a leap year, False otherwise"
    if year % 400 == 0:
        return True       # divisible by 400: always a leap year
    if year % 100 == 0:
        return False      # divisible by 100 but not 400: not a leap year
    if year % 4 == 0:
        return True       # divisible by 4 but not 100: leap year
    return False          # all other years are not leap years

def mon_max(month: int, year: int) -> int:
    "Returns the maximum day for a given month. Includes leap year check"
    feb_days = 29 if leap_year(year) else 28  # feb has 29 days in leap year, 28 otherwise
    month_days = {1:31, 2:feb_days, 3:31, 4:30, 5:31, 6:30,
                  7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    return month_days[month]  # return the max days for the given month

def after(date: str) -> str:
    '''
    after() -> date for next day in YYYY-MM-DD string format

    Return the date for the next day of the given date in YYYY-MM-DD format.
    This function takes care of the number of days in February for leap year.
    This function has been tested to work for year after 1582
    '''
    str_year, str_month, str_day = date.split('-')  # split date string into 3 parts
    year = int(str_year)    # convert year string to integer
    month = int(str_month)  # convert month string to integer
    day = int(str_day)      # convert day string to integer

    tmp_day = day + 1  # calculate tomorrow by adding 1 to current day

    if tmp_day > mon_max(month, year):
        # tomorrow exceeds this month's last day, so roll over to 1st of next month
        to_day = 1
        tmp_month = month + 1  # move to next month
    else:
        to_day = tmp_day   # tomorrow is still within the current month
        tmp_month = month  # month does not change

    if tmp_month > 12:
        to_month = 1       # if we go past December, roll over to January
        year = year + 1    # and increment the year by 1
    else:
        to_month = tmp_month  # month is still within valid range

    next_date = f"{year}-{to_month:02}-{to_day:02}"  # format as YYYY-MM-DD
    return next_date

def usage():
    "Print a usage message to the user"
    print("Usage: assignment1.py YYYY-MM-DD YYYY-MM-DD")
    sys.exit(1)

def valid_date(date: str) -> bool:
    "Check validity of date and return True if valid"
    ...

def day_count(start_date: str, stop_date: str) -> int:
    "Loops through range of dates, and returns number of weekend days"
    ...

if __name__ == "__main__":
    pass
