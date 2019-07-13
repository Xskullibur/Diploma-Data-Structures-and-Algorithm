# # Binary Search
# def binarySearch(array, target):
#
#     low = 0
#     high = len(array)
#     result = -1
#
#     while low < high:
#         mid = (high + low)//2
#
#         if array[mid] == target:
#             result = mid
#             high = mid-1
#
#         elif array[mid] > target:
#             high = mid - 1
#
#         else:
#             low = mid + 1
#
#     return result


# # Selection Sort
# def selectionSort(array, sortType):
#
#     n = len(array)
#
#     for i in range(n - 1):
#
#         smallIndex = i
#
#         if sortType == 'D':
#             for j in range(i+1, n):
#                 if array[j] > array[smallIndex]:
#                     smallIndex = j
#
#         elif sortType == 'A':
#             for j in range(i+1, n):
#                 if array[j] < array[smallIndex]:
#                     smallIndex = j
#
#         if smallIndex != i:
#             temp = array[i]
#             array[i] = array[smallIndex]
#             array[smallIndex] = temp


# Insertion Sort
def insertionSort(array):

    n = len(array)

    for i in range(1, n):

        value = array[i]

        pos = i
        while pos > 0 and value < array[pos-1]:
            array[pos] = array[pos-1]
            pos -= 1

        array[pos] = value


testArray = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
insertionSort(testArray)

# # Sort from accending with those beginning with 'H' infront
# def specialSort(array):
#
#     n = len(array)
#     hArray = []
#     otherArray = []
#
#     for i in range(0, n):
#
#         if array[i][:1] == ('H' or 'h'):
#             hArray.append(array[i])
#
#         else:
#             otherArray.append(array[i])
#
#     return sorted(hArray) + sorted(otherArray)
#
#
# # Tuple Sort
# def sortTuple(array):
#     return sorted(array, key=lambda x: x[1])
#
#
# # Fibonacci Sequence
# def fib(n):
#     if n > 1:
#         return fib(n-1) + fib(n-2)
#
#     elif n == 1 or n == 0:
#         return n
#
#
# # Recursive Binary
# def recBinarySearch(target, array, first, last):
#
#     if first > last:
#         return False
#
#     else:
#         mid = (first + last) // 2
#
#         if array[mid] == target:
#             return mid
#
#         elif target < array[mid]:
#             return recBinarySearch(target, array, first, mid-1)
#
#         else:
#             return recBinarySearch(target, array, mid+1, last)
#
#
# # Split Odd Numbers and Even Number
# def evenOdd(array, first, last):
#
#     if first < last:
#
#         if array[last] % 2 == 0:
#             temp = array[first]
#             array[first] = array[last]
#             array[last] = temp
#
#             return evenOdd(array, first, last-1)
#
#         else:
#             return evenOdd(array, first+1, last)
#
#     else:
#         return array
