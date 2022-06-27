def reverseWordsInString(string):
    if len(string) == 0:
        return ""

    stringArr = []
    tmp_Str = ""

    for i in string:
        if i == " ":
            stringArr.append(tmp_Str)
            tmp_Str = ""
        else:
            tmp_Str = tmp_Str + i
    
    stringArr.append(tmp_Str)

    reverse_arr = get_reverse(stringArr)

    res = " ".join(reverse_arr)
    return res


def get_reverse(arr):
    l = 0
    r = len(arr) - 1

    while l <= r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1

    return arr


string =  "AlgoExpert is the best!"
print(reverseWordsInString(string))