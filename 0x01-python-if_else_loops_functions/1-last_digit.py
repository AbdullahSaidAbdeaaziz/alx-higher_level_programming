#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


def check_number(number):
    if number < 6 and number:
        return " and is less than 6 and not 0"
    elif number > 5:
        return " and is greater than 5"
    else:
        return " and is 0"


if number < 0:
    number = -number
    last_number = -(number % 10)
    print(f"Last digit of {-number} is {last_number}\
{check_number(last_number)}")
else:
    last_number = number % 10
    print(f"Last digit of {number} is {last_number}\
{check_number(last_number)}")
