# def maxConsecutive(bottom, top, special):
#     count = 0
#     for i in special:
#         if i > bottom:
#             if i - bottom > 1:
#                 count += 1
#             bottom = i
#             print(f"bottom: {bottom}")

#     if top > bottom:
#         if top - bottom > 1:
#             count += 1
#     return count


# # bottom = 6
# # top = 8
# # special = [7,6,8]

# bottom = 2
# top = 9
# special = [4,6]

# print(maxConsecutive(bottom, top, special))




def getProd(arr):
    res = [0 for i in range(len(arr))]
    i = 0
    while i < len(arr):
        res[i] = mul(arr[:i]) * mul(arr[i+1:])
        print(arr[:i], arr[i+1:])
        i += 1
    return res

def mul(num):
    prod = 1
    for i in num:
        prod *= i
    return prod

arr = [1,2,3,4]
print(getProd(arr))

