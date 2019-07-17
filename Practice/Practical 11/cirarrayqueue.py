class Queue:

    def __init__(self, maxSize):
        self._count = 0
        self._front = 0
        self._back = maxSize - 1
        self._qArray = [None] * maxSize

    def isEmpty(self):
        return self._count == 0

    def isFull(self):
        return self._count == len(self._qArray)

    def __len__(self):
        return self._count

    def enqueue(self, item):
        assert not self.isFull(), "Cannot enqueue to a full queue."
        maxSize = len(self._qArray)
        self._back = (self._back + 1) % maxSize
        self._qArray[self._back] = item
        self._count += 1

    def dequeue(self):
        assert not self.isEmpty(), "Cannot dequeue from an empty queue"
        item = self._qArray[self._front]
        maxSize = len(self._qArray)
        self._front = (self._front - 1) % maxSize
        self._count -= 1
        return item

    def __str__(self):
        maxSize = len(self._qArray)
        outStr = ''
        for i in range(self._count):
            outStr += ('[' + str((self._front + i) % maxSize) + ']:')
            outStr += (str(self._qArray[(self._front + i) % maxSize]) + ' ')
        return outStr


newQueue = Queue(5)
newQueue.enqueue(10)
newQueue.enqueue(20)
newQueue.enqueue(30)
newQueue.enqueue(40)
newQueue.enqueue(50)

print("After enqueuing 5 items to an empty queue")
print(str(newQueue))

newQueue.dequeue()
newQueue.dequeue()

print("After dequeuing 2 items from the queue")
print(str(newQueue))

newQueue.enqueue(60)
newQueue.enqueue(70)

print("After enqueuing 2 more items to the queue")
print(str(newQueue))
