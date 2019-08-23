# Ascending Sort
# =======================================================================================
# Loop though the array
# Foreach index loop though the values before the index
# Push all the values before and larger than the index up an index and place the index

def insertionSort(seq):
    n = len(seq)

    for i in range(1, n):
        value = seq(i)

        pos = i
        while pos > 0 and value < seq(pos - 1):
            seq[pos] = seq[pos - 1]
            pos -= 1

        seq[pos] = value