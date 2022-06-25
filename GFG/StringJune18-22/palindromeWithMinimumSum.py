def minimumSum(s):
    if ord(s[0]) in range(97, 122)
    mid = len(s)//2 if len(s) % 2 == 0 else (len(s)//2) + 1
    
    count = 0
    for i in range(mid):
        if s[i] != s[len(s)-1-i]:
            if ord(s[i]) in range(97, 122):
                if ord(s[len(s)-1 - i]) in range(97, 122):
                    return -1
                elif s[i] == '?' or s[len(s)-1-i] == '?':
                    count += 1

    return count 
    # for i in range(mid):
    #     if 97 <= ord(s[i]) <= 122 and 97 <= ord(s[i+mid]) <= 122:
    #         if s[]

S = "a???c??c????"
print(minimumSum(S))