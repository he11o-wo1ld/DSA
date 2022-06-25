from collections import Counter
def rearrangeCharacters(s, target):
    count1=Counter(s)
    count2=Counter(target)
    res=0
    check=True
    while(check):
        for ch in target:
            if(count1[ch]>0):
                count1[ch]-=1
            elif(count1[ch]==0):
                check=False
                break
        if(check):      
            res+=1
    return res
    # si = 0
    # ti = 0
    
    # count = 0
    # res = 0
    # while si < (len(s)) and ti < len(target):
    #     if s[si] == target[ti]:
    #         count += 1
    #         si += 1
    #         ti += 1
            
    #         if count == len(target):
    #             res += 1
    #             ti = 0
    #     else:
    #         si += 1
    # return res
    
s = "ilovecodingonleetcode"
target = "code"

print(rearrangeCharacters(s, target))