# time : O(n) | space : O(n)
def nextGreaterElement(array):
    result = [-1 for i in array]
    stack = []

    # for idx in range(len(array)): # single loop
    for idx in range(2 * len(array)):   # double loop
        circular_idx = idx % len(array)

        while len(stack) > 0 and array[stack[len(stack) - 1]] < array[circular_idx]:
            top = stack.pop()
            result[top] = array[circular_idx]

        stack.append(circular_idx)
    return result



array = [2, 5, -3, -4, 6, 7, 2]
print(nextGreaterElement(array))
