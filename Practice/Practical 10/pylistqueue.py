class Queue:

    def __init__(self):
        self._qList = list()

    def __len__(self):
        return len(self._qList)

    def isEmpty(self):
        return True if len(self._qList) == 0 else False

    def enqueue(self, item):
        self._qList.insert(len(self._qList), item)

    def dequeue(self):
        assert not self.isEmpty(), "Cannot dequeue empty queue"
        return self._qList.pop(0)


newQueue = Queue()
while True:
    try:
        newQueue.enqueue(input("Enter a number (ctrl-D to end):"))
    except EOFError:
        break

while not newQueue.isEmpty():
    print(newQueue.dequeue())