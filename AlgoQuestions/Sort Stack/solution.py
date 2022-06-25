def sortStack(stack):
    if len(stack) == 0:
        return stack

    top = stack.pop()

    sortStack(stack)

    insertIntoSortedOrder(stack, top)

    return stack

def insertIntoSortedOrder(stack, top):
    if len(stack) == 0 or stack[len(stack)-1] <= top:
        stack.append(top)
        return
    
    current_top = stack.pop()
    insertIntoSortedOrder(stack, top)

    stack.append(current_top)

stack = [-5, 2, -2, 4, 3, 1]
print(sortStack(stack))
