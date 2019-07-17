from timer import timeit
import random

@timeit
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

    # print(theList)
    # print("First:", theList[first])
    # print("Last:", theList[right], "\n")
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


def getTestArray(size):
    return [random.randrange(1, 3000) for i in range(size)]


array1 = getTestArray(1000)
print("Original:", array1)
hybridSort(array1, 0, len(array1)-1)
print("Sorted:", array1)