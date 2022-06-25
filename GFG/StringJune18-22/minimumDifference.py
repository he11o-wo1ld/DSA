def minimumDifference(arr, S):
	res = []
	for i in arr:
		s = getCount(S, i)
		res.append(s)
	op = min(res)
	return op

def getCount(s1, s2):
	count = 0
	s_dict = {}
	for i in s1:
		if i not in s_dict:
			s_dict[i] = 1
		else:
			s_dict[i] += 1

	for i in s2:
		if i not in s_dict:
			count += 1
	return count


S = "abcde"
arr = ["cdf","efd","klda","eaf"]
print(minimumDifference(arr, S))