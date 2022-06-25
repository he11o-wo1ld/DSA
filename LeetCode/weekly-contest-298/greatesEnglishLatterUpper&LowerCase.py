def greatestLetter(s):
    ascci_value = {}
    for i in s:
        if ord(i) not in ascci_value:
            ascci_value[ord(i)] = [i]
        else:
            ascci_value[ord(i)].append(i)

        if ord(i) + 32 in ascci_value:
            return i
    return ''


s = "nzmguNAEtJHkQaWDVSKxRCUivXpGLBcsjeobYPFwTZqrhlyOIfdM"
print(greatestLetter(s))