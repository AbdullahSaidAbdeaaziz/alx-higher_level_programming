#!/usr/bin/python3
result = ""
for i in range(99):
    result += f"{i} = {hex(i)}\n"
print("{result}".format(result),end="")
