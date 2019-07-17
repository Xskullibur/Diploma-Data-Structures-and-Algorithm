class Queue:
    def __init__(self):
        self._qList = list()

    def isEmpty(self):
        return len(self._qList) == 0

    def __len__(self):
        return len(self._qList)

    def enqueue(self, item):
        self._qList.append(item)

    def dequeue(self):
        assert not self.isEmpty(), \
            "Cannot dequeue from an empty queue"
        return self._qList.pop(0)


newQueue = Queue()

while True:
    try:
         newQueue.enqueue(input("Enter a number (Ctrl-D to end): "))
    except EOFError:
        break

print("The contents of the queue:")
while not newQueue.isEmpty():
    print(newQueue.dequeue(), end=" ")