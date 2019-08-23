# Ascending Sort
# =================================================================
# Loop though the array
# For each index, loop though the array again
# Look for the smallest value in the array
# Swap the value of the index with the smallest value in the array

def selectionSort(seq):
    n = len(seq)

    for i in range(n - 1):
        smallNdx = i

        for j in range(i+1, n):
            if seq[j] < seq[smallNdx]:
                smallNdx = j

        if smallNdx != i:
            tmp = seq[i]
            seq[i] = seq[smallNdx]
            seq[smallNdx] = tmp