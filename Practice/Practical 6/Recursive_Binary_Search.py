def recBinarySearch(target, theValues, first, last):

    if (first > last):
        return False

    else:
        mid = (first + last) // 2

        if (theValues[mid] == target):
            print(theValues[mid])
            return True

        elif target < theValues[mid]:
            return recBinarySearch(target, theValues, first, mid-1)


        else:
            return recBinarySearch(target, theValues, mid + 1, last)


list = [1, 2, 4, 7, 9, 10, 11, 14, 19]
print(recBinarySearch(12, list, 0, len(list) - 1))
print(recBinarySearch(7, list, 0, len(list) - 1))
print(recBinarySearch(2, list, 0, len(list) - 1))