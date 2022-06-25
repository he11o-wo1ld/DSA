def minimumChanges(s):
    l = 0
    r = len(s) - 1
    count = 0
    while l <= r:
        if s[l] != s[r]:
            count += 1
        l += 1
        r -= 1
    return count
        
s = "abdc"
print(minimumChanges(s))