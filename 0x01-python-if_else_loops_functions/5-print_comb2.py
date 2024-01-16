#!/usr/bin/python3
result = ""
for i in range(100):
    if i < 10:
        result += f"0{i}"
    else:
        result += f"{i}"
    if i != 99:
        result += f", "
print("{}".format(result))
