def hybridSort(array, low, high):

    while low < high:
        if high - low <= 10:
            insertionSort(array)
            break

        else:
            pivot = quickSort(array, low, high)

            if pivot - low < high - pivot:
                hybridSort(array, low, pivot - 1)
                low = pivot + 1
            else:
                hybridSort(array, pivot + 1, low)
                high = pivot - 1


def quickSort(theList, first, last):

    pivot = theList[first]

    left = first + 1
    right = last

    while left <= right:

        # Scan until the value is equal / larger than pivot or right marker
        while left <= right and theList[left] < pivot:
            left += 1

        # Scan until the value is equal / smaller than pivot or left marker
        while left <= right and theList[right] > pivot:
            right -= 1

        # Cross the right and left
        if left <= right:

            # Swap the left and right values
            theList[left], theList[right] = theList[right], theList[left]

            # Shrink the range towards the base case
            left += 1
            right -= 1

    print(theList)
    print("First:", theList[first])
    print("Last:", theList[right], "\n")
    # Move the position of the pivot to the right index (Proper Position)
    theList[first], theList[right] = theList[right], theList[first]

    return right


def insertionSort(array):

    n = len(array)

    for i in range(1, n):
        val = array[i]
        pos = i

        while pos > 0 and val < array[pos - 1]:
            array[pos] = array[pos-1]
            pos -= 1

    array[pos] = val


testArray1 = [9, 12, 5, 40, 1, 32, 50, 45, 22, 18, 42]
testArray2 = [12, 16, 41, 24, 11, 19, 33, 28, 40, 38, 46, 20, 18, 27, 30, 14, 21, 4, 9, 39, 15, 8, 25, 48, 6, 5, 10, 3, 50, 13, 35, 37, 2, 34, 29, 22, 23, 43, 45, 17, 31, 44, 32, 1, 7, 26, 42, 47, 36, 49]

print("Original:", testArray1)
hybridSort(testArray1, 0, len(testArray1)-1)
print("Sorted:", testArray1)