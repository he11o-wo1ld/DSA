def sortStack(stack):
    if len(stack) <= 1:
        return stack

    valueOne = stack.pop()

    sortStack(stack)
    
    valueTwo = stack.pop()

    smallerValue = valueOne if valueOne < valueTwo else valueTwo
    largerValue = valueTwo if valueOne < valueTwo else valueOne

    stack.append(smallerValue)
    sortStack(stack)
    stack.append(largerValue)

    return stack

stack = [-5, 2, -2, 4, 3, 1]
print(sortStack(stack))
