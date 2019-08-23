def multiply (x, y):
    if x == 0:
        return 0
    elif x == 1:
        return y
    else:
        return multiply(x-1, y) + x


print(multiply(4, 4))