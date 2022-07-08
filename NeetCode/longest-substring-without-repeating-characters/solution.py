def lengthOfLongestSubstring(s):
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
                while s[r] in charSet:
                        charSet.remove(s[l])
                        l += 1
                charSet.add(s[r])
                res = max(res, r - l + 1)
        return res

        # nonRepeating = {}
        # count = 0
        # res = 0

        # for i in range(len(s)):
        #     if s[i] not in nonRepeating:
        #         nonRepeating[s[i]] = i
        #         count += 1
        #     elif s[i] in nonRepeating:
        #         while s[i] in nonRepeating:
        #             nonRepeating.pop(s[i])
        #             count -= 1
        #     res = max(res, count)
        # return res



s = "abcabcbb"
print(lengthOfLongestSubstring(s))