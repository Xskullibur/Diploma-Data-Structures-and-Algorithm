def quickSort(theList):
    n = len(theList)
    recQuickSort(theList, 0, n-1)


def recQuickSort(theList, first, last):
    if first >= last:
        return
    else:
        pos = partitionSeq(theList, first, last)

        recQuickSort(theList, first, pos - 1)
        recQuickSort(theList, pos + 1, last)


def partitionSeq(theList, first, last):

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


listOfNo = [12, 7, 9, 24, 7, 29, 5, 3, 11, 7]

print("Input List:", listOfNo)
quickSort(listOfNo)
print("Sorted List:", listOfNo)

