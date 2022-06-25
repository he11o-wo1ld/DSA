# def compres(nums):
# 	count = 0
# 	curr = ""
# 	res = ""

# 	for i in range(1,len(nums)):
# 		curr = nums[i-1]
# 		if nums[i] == curr:
# 			count += 1

# 		elif nums[i] != curr:
# 			print(curr, nums[i])
# 			res += f"{count}{curr}"
# 			count = 1
# 			curr = nums[i]
# 			print(curr)
# 	return res

nums = "aaabbcc"


def compress(chars):
	i = 0
	count = 1
	for j in range(1, len(chars) + 1):
		if j < len(chars) and chars[j] == chars[j-1]:
			count += 1

		else:
			chars[i] = chars[j-1]
			i += 1
			if count > 1:
				for k in str(count):
					chars[i] = k
					i += 1
			count = 1
	return i


chars = ["a","a","b","b","c","c","c"]
print(compress(chars))