def mergeSort( theList ):

    if len(theList) <= 1:
        return theList
    else:

        mid = len(theList) // 2

        leftHalf = mergeSort(theList[:mid])
        rightHalf = mergeSort(theList[mid:])

        newList = mergeSortedList(leftHalf, rightHalf)
        return newList


def mergeSortedList(listA, listB):

    newList = []
    a = 0
    b = 0

    while a < len(listA) and b < len(listB):
        if listA[a] < listB[b]:
            newList.append(listA[a])
            a += 1
        else:
            newList.append(listB[b])
            b += 1

    while a < len(listA):
        newList.append(listA[a])
        a += 1

    while b < len(listB):
        newList.append(listB[b])
        b += 1

    return newList


listOfNo = [12, 7, 9, 24, 7, 29, 5, 3, 11, 7]

print('Input List:', listOfNo)
merge_list = mergeSort(listOfNo)
print('Sorted List:', merge_list)