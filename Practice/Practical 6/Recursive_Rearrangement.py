# def recSort(theValues, index):
#
#     lastIndex = (len(theValues) - 1) - index
#
#     if (index > lastIndex):
#         return theValues
#
#     elif (theValues[index] % 2 == 1):
#         temp = theValues[index]
#         theValues[index] = theValues[lastIndex]
#         theValues[lastIndex] = temp
#
#     return recSort(theValues, index + 1)


def recsort2(data, low, high):

    if(low < high):

        if(data[high] % 2 == 0):
            temp = data[high]
            data[high] = data[low]
            data[low] = temp

            return recsort2(data, low + 1, high)
        else:
            return recsort2(data, low, high - 1)

    else:
        return data


# print(recSort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0))
print(recsort2([1, 2, 3, 4, 5, 6, 7, 9, 10, 12, 13, 15, 19, 20], 0, 13))