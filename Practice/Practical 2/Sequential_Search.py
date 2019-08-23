# let n be the length of the values
# loop though each values in the array and look for the target value
# if the value is found return True
# else if you looped though the whole array and target value not found return False

def sequentialSearch(values, target):
    n = len(values)

    for i in range(n):
        if values[i] == target:
            return True

    return False