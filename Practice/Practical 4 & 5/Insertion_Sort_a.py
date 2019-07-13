# Function that takes in a list of strings but return those begining with 'H'
def sortList(input):

    hList = []
    otherList = input

    for i in input:
        if i[0] == 'H':
            hList.append(i)
            otherList.remove(i)

    otherList = sorted(otherList)
    hList = sorted(hList)
    print(sorted(hList) + sorted(otherList))


list_of_no = ['Bougainvillea', 'Orhcids', 'Hibiscus', 'Frangipani', 'Honeysuckle']
sortList(list_of_no)