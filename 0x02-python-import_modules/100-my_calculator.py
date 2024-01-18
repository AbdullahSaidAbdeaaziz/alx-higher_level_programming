#!/usr/bin/python3

if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit

    size_args = len(argv) - 1
    if size_args != 3:
        print(r"Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    operator = argv[2]
    operators = "+-*/"
    if operator not in operators or len(operator) > 1:
        print(r"Unknown operator. Available operators: +, -, * and /")
        exit(1)

    first_num = int(argv[1])
    second_num = int(argv[3])
    if operator == "+":
        print(
            "{} {} {} = {}".format(
                first_num,
                operator,
                second_num,
                add(first_num, second_num)
                )
            )
    elif operator == "-":
        print(
            "{} {} {} = {}".format(
                first_num,
                operator,
                second_num,
                sub(first_num, second_num)
                )
            )
    elif operator == "*":
        print(
            "{} {} {} = {}".format(
                first_num,
                operator,
                second_num,
                mul(first_num, second_num)
                )
            )
    else:
        print(
            "{} {} {} = {}".format(
                first_num,
                operator,
                second_num,
                div(first_num, second_num)
                )
            )
