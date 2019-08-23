# define the min value as the first index
# define the max value as the last index
# continue the loop while the min value is lesser than max value
# define the mid value of min and max
# if the mid value is the target value return mid value
# else if target value is lesser than the middle value change max value to mid-1
# else change max value to mid+1
# if high more than low return -1

def binarySearch(values, target):
    low = 0
    high = len(values)-1

    while high > low:
        mid = high + low // 2

        if values[mid] == target:
            return mid

        elif target < values[mid]:
            high = mid - 1

        else:
            low = mid + 1

    return -1