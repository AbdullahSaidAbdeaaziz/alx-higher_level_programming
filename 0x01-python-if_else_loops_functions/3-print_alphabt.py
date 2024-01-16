#!/usr/bin/python3
result = ""
for i in range(97, 123):
    if chr(i) == 'e' or chr(i) == 'q':
        continue
    result += chr(i)
print("{}".format(result), end="")
