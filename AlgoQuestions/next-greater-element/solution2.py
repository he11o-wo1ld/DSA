# time : O(n) | space : O(n)
def nextGreaterElement(array):
    result = [-1 for i in array]
    stack = []

    for idx in range(2 * len(array)-1, -1, -1):
        circular_idx = idx % len(array)

        while len(stack) > 0:
            if stack[len(stack) - 1] <= array[circular_idx]:
                stack.pop()
            else:
                result[circular_idx] = stack[len(stack) - 1]
                break
        stack.append(array[circular_idx])
    return result


array = [2, 5, -3, -4, 6, 7, 2]
print(nextGreaterElement(array))
