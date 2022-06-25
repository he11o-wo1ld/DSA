class Car:
    def __init__(self, color, type):
        self.color = color
        self.type = type


VW = Car("Blue", "Street")

print(VW.color)


# def function(nums):
#     current = 0
#     # nums_dict = {}
#     res = ""
#     for i in range(len(nums)):
#         count = 0
#         if nums[i] == nums[current]: #a, a
#             count += 1
#         res += f"{count}{nums[i]}"
#         current = i
#     return res

# #nums[current] = a
# #nums[i] = a
# #count = 3

# nums = "aaabbccccaa"
# print(function(nums))