# time: O(n^2) | space: O(n)

def longestPalindromicSubstring(string):
    if len(string) == 1:
        return string
        
    current_longest = [0, 1]
    
    for i in range(1, len(string)):
        odd = getLongestPalindromeFrom(string, i-1, i+1)
        even = getLongestPalindromeFrom(string, i-1, i)
         
        longest = max(even, odd, key=lambda x:x[1] - x[0])
        
        current_longest = max(longest, current_longest, key=lambda x: x[1] - x[0])
        
    return string[current_longest[0]:current_longest[1]]
    
def getLongestPalindromeFrom(string, leftIdx, rightIdx):
    while leftIdx >= 0 and rightIdx < len(string):
        if string[leftIdx] != string[rightIdx]:
            break
        leftIdx -= 1
        rightIdx += 1
        
    return [leftIdx+1, rightIdx]


string = "abaxyzzyxf"
print(longestPalindromicSubstring(string))
