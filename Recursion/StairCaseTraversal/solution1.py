def fact(n):
    if n == 1:
        return 1
    return fact(n-1) * n

def findNum(n):
    num = 1

    while n != 0:
        facto = fact(num)
        rev = str(facto)
        for i in range(len(rev)-1,-1, -1):
            if rev[i] == 0:
                n -= 1
            else:
                num += 1
    return num


n = 1
print(findNum(n))