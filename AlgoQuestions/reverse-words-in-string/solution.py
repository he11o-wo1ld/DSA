def reverseWordsInString(string):
    # Write your code here.
    strings = string.split(" ")
    strings.reverse()
    res = " ".join(strings)
    return res

string =  "AlgoExpert is the best!"
print(reverseWordsInString(string))