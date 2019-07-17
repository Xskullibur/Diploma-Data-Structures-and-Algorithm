import time

def timeit(func):
    def wrapper(*args, **kw):
        startTime = time.time()
        func(*args, **kw)
        endTime = time.time()

        timeDiff = endTime - startTime

        print("Time Elapse: ", timeDiff * 1000)
    return wrapper