#!/usr/bin/python3
result = ""
for i in range(122, 96, -1):
    if i % 2 != 0:
        result += chr(i).upper()
    else:
        result += chr(i)
print("{}".format(result), end="")
