def stringPartition(S,a,b):
    num1 = ""
    num2 = ""
    res = ""
    l = len(S)
    i = 1
    while i < l:
        first = S[:i]
        second = S[i:]
        
        if int(first) % a == 0 and int(second) % b == 0:
            num1 = first
            num2 = second
            res = num1 + " " + num2
            return f"{num1} {num2}"
        i += 1
    return

S = "125"
a = 12
b = 5
print(stringPartition(S, a, b))



print(S[a:])
