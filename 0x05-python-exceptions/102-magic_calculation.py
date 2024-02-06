#!/usr/bin/python
# from dis import dis
def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("too far")
            result += a ** b / i
        except Exception:
            result = a + b
            break
    return result
# print(dis(magic_calculation))
