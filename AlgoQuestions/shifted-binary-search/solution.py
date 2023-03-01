def shiftedBinarySearch(array, target):
    # Write your code here.
    n = len(array)
    break_point = find_break(array)

    if target > array[break_point] or target < array[(break_point + 1)%n]:
        return -1

    if target >= array[0]:
        return search(array, 0, break_point, target)
        
    return search(array, break_point + 1, len(array) - 1, target)


def find_break(array):
    n = len(array) - 1
    l, r = 0, n
    while r >= l:
        mid = l + (r - l) // 2

        if mid == n or array[mid] > array[mid + 1]:
            return mid

        if array[mid] < array[l]:
            r = mid - 1

        else:
            l = mid + 1


def search(array, start, end, target):
    l, r = start, end
    while r >= l:
        mid = l + (r - l) // 2
        if array[mid] == target:
            return mid

        if array[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1


array = [45, 61, 71, 72, 73, 0, 1, 21, 33, 37]
target = 33
print(shiftedBinarySearch(array, target))









