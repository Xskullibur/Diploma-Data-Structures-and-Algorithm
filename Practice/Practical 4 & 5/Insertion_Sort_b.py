# Takes in non empty list of tuples and return list sorted by last element of tuple
def sortInput(seq):
    print(sorted(seq, key=lambda x: x[-1]))


input = [(1, 7), (1, 3), (3, 4, 5), (2, 2)]
sortInput(input)