# time : O(n) | space : O(1), where n is the length of the array
def threeNumberSort(array, order):
    values = [0 for i in order]

    for element in array:
        olderIdx = order.index(element)
        values[olderIdx] += 1

    for i in range(3):
        value = order[i]
        count = values[i]

        numElementsBefore = sum(values[:i])

        for n in range(count):
            currentIdx = numElementsBefore + n
            array[currentIdx] = value

    return array

    # for i in order:
    #     first = 0
    #     second = 0
    #     last = len(array) - 1
    #     while first <= last or second <= last:
    #         if array[first] == i:
    #             array[first], array[second] = array[second], array[first]
    #             first += 1
    #             second += 1
    #         else:
    #             second += 1

    # return order

array = [1, 0, 0, -1, -1, 0, 1, 1]
order = [0, 1, -1]
print(threeNumberSort(array, order))
