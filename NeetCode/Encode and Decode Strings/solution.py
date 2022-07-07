def encode(strs):
    res = ""
    for s in strs:
        res += str(len(s)) + "#" + s
    return decode(res)

def decode(string):
    res = []
    i = 0

    while i < len(string):
        j = i
        while str[j] != "#":
            j += 1
        length = int(str[i:j])
        res.append(str[j+1:j+1+length])
        i = j + 1 + length
    return res


strs = ["lint","code","love","you"]
print(encode(strs))