class stack:

    def __init__(self):
        self._theItems = list()

    def isEmpty(self):
        if len(self._theItems) == 0:
            return True
        else:
            return False

    def __len__(self):
        return len(self._theItems)

    def peek(self):
        assert not self.isEmpty(), "Cannot peak at an empty stack"
        return self._theItems[-1]

    def pop(self):
        assert not self.isEmpty(), "Cannot pop from empty stack"
        str = self._theItems[-1]
        self._theItems.pop()
        return str

    def push(self, item):
        self._theItems.append(item)


# newStack = stack()
#
# while True:
#     try:
#         print("Enter a number (ctrl-D to end) :")
#         newStack.push(input())
#
#     except EOFError:
#         break
#
# print("Contents if the stack:")
#
# while not newStack.isEmpty():
#     print(newStack.pop())