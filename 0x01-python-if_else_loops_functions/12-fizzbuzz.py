#!/usr/bin/python3
def check_fizz_buzz(number):
    result = ""
    if number % 3 == 0:
        result += "Fizz"
    if number % 5 == 0:
        result += "Buzz"
    return result


for i in range(1, 101):
    is_fizz_buzz = check_fizz_buzz(i)
    if not is_fizz_buzz:
        print(i, end="")
    print(is_fizz_buzz, end="")
    if i != 100:
        print(" ", end="")
print()
