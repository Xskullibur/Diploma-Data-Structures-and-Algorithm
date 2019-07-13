def sort(array, first, last):

    value = first

    if first < last:

        for i in range(first+1, last):
            if array[i] > array[value]:
                value = i

        if value != first:
            array[first], array[value] = array[value], array[first]

        return sort(array, first+1, last)

    return array


testArray = [10, 20, 30, 20, 30, 10, 30, 10, 20]
print(sort(testArray, 0, len(testArray)))