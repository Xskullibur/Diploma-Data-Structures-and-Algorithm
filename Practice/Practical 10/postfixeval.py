from pyliststack import stack

print("Postfix Expression Evaluator")
print("For help, type \"help\" or \"?\"")
print("To quit, type \"quit\" or \"q\"")

while True:
    expression = input("\nEnter a Postfix expression to be evaluated: ")
    tokens = expression.split(" ")

    myStack = stack()

    if tokens[0] == "help" or tokens[0] == "?":
        print("Postfix Expression Evaluator takes in a mathematical expression expressed in Postfix notation and evaluate it")
        print("Example: \"1 2 + 4 *\" will evaluate to \"12\"")

    elif tokens[0] == "quit" or tokens[0] == "q":
        break

    else:
        valid = True
        while len(tokens) > 0:
            item = tokens.pop(0)

            if item.isdigit():
                myStack.push(int(item))

            # Handle "+" Operand
            elif item == "+":
                if len(myStack) > 1:
                    myStack.push(myStack.pop() + myStack.pop())
                else:
                    valid = False
                    break

            # Handle "-" Operand
            elif item == "-":
                if len(myStack) > 1:
                    item1 = myStack.pop()
                    item2 = myStack.pop()
                    myStack.push(item2 - item1)
                else:
                    valid = False
                    break

            # Handle "*" Operand
            elif item == "*":
                if len(myStack) > 1:
                    item1 = myStack.pop()
                    item2 = myStack.pop()
                    myStack.push(item2 * item1)
                else:
                    valid = False
                    break

            # Handle "/" Operand
            elif item == "/":
                if len(myStack) > 1:
                    item1 = myStack.pop()
                    item2 = myStack.pop()
                    myStack.push(item2 / item1)
                else:
                    valid = False
                    break

            # Handle "^" Operand
            elif item == "^":
                if len(myStack) > 1:
                    item1 = myStack.pop()
                    item2 = myStack.pop()
                    myStack.push(item2 ** item1)
                else:
                    valid = False
                    break

            else:
                valid = False
                break

        if myStack.__len__() != 1:
            valid = False

        if valid:
            print("Evaluation Result: ", myStack.pop())
        else:
            print("Invalid Postfix expression!")
