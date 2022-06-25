def selectionSort(array):
    # Write your code here.
    currentIndex = 0
    while currentIndex < len(array) - 1:
        smallIndex = currentIndex
        for i in range(currentIndex + 1, len(array)):
            if array[smallIndex] > array[i]:
                smallIndex = i
        swap(currentIndex, smallIndex, array)
        currentIndex += 1
    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
