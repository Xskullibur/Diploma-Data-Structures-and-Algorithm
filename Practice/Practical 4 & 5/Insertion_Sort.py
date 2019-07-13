def insertionSort(theSeq):
    n = len(theSeq)
    print("Pass:  0", theSeq)

    for i in range(1, n):
        value = theSeq[i]
        pos = i

        while pos > 0 and value < theSeq[pos - 1]:
            theSeq[pos] = theSeq[pos - 1]
            pos -= 1

        print("Pass: ", i, theSeq)
        theSeq[pos] = value


list_of_no = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]

insertionSort(list_of_no)