from collections import defaultdict
str = ["eat", "tea", "tan", "ate", "nat", "bat"]
def group_anagram(str):
	res = defaultdict(list)

	for s in str:
		count = [0] * 26

		for c in s:
			count[ord(c) - ord("a")] += 1
			# print(count, ord(c))

		res[tuple(count)].append(s)
		# print(res)
	return res.values()


# def anagram(str1, str2):
# 	if len(str1) != len(str2):
# 		return False
# 	str1_dict = {}
# 	str2_dict = {}
# 	for i in range(len(str1)):
# 		if str1[i] not in str1_dict:
# 			str1_dict[str1[i]] = 1
# 		else:
# 			str1_dict[str1[i]] += 1
# 	for i in range(len(str2)):
# 		if str2[i] not in str2_dict:
# 			str2_dict[str2[i]] = 1
# 		else:
# 			str1_dict[str1[i]] += 1
# 	return str1_dict == str2_dict


print(group_anagram(str))