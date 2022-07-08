""" Def List Comprehension(list1, list2):
    L1 = 0
    L2 = 0
    
    Result = []

    While l1 < len(list1) - 1 or l2 < len(list2):
        If list1[l1] > list2[l2]:
            result.apped(list2[l2])
            L2 += 1
        If list2[l2] > list1[l1]:
            result.append(list1[l1])

Touple = (1, 2, 3)

# Dic = {“a”:1,{“b”:2}}
Find value of a

Dic[a] 
# Dic = {“a” : {“b”:2}}


List1 = [1, 3, 5]
List2 = [2, 4, 8]


Arr = [1,-2,3,1,4]
3,1,4 =8
Max sum of largest contiguous array
"""

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")

my_dic = {'a': 1}
for i in my_dic:
    print(my_dic[i])
print(my_dic['a'])

arr = [1, 2, 3, 4]
def GetReverse(arr):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        swap(left, right, arr)
        left += 1
        right -= 1
    return arr
    


def swap(l, r, arr):
    arr[l], arr[r] = arr[r], arr[l]
    
print(GetReverse(arr))


Arr = [1,-2,3,1,4]

def maxSum(arr):
    minimum = arr[0]
    maxsum = 0
    currSum = arr[0]
    
    for i in range(len(arr)):
        if minimum > arr[i]:
            minimum = arr[i+1]
            continue
        
        else:
            if currSum + arr[i] > 0:
                currSum = max(arr[i], currSum + arr[i])
            maxsum = max(maxsum, currSum)
        
    return maxsum

def kadence(a):
    max_so_far =a[0]
    curr_max = a[0]

    for i in range(1,len(a)):
        curr_max = max(a[i], curr_max + a[i])
        max_so_far = max(max_so_far,curr_max)
    
    return max_so_far

print(maxSum(Arr))
print(kadence(Arr))

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

