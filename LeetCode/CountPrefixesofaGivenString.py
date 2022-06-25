def countPrefixes(words, s):
    if len(s) <= 1:
        char1 = s
    else:
        char1 = s[0]
    
    count = 0
    
    for i in words:
        if len(i) <= 1:
            if i == char1:
                count += 1

        elif len(i) > 1:
            char2 = i[0]
            if char2 == char1:
                count += 1
    
    return count

words = ["feh","w","w","lwd","c","s","vk","zwlv","n","w","sw","qrd","w","w","mqe","w","w","w","gb","w","qy","xs","br","w","rypg","wh","g","w","w","fh","w","w","sccy"]
s = "w"

print(countPrefixes(words, s))

print("w" == "W")