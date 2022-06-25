def count(array):
	res = ""
	previous = ""
	count = 0

	i = 0

	while i < len(array):
		if previous == "":
			previous = array[i]
			count += 1

		elif previous == array[i]:
			count += 1

		elif previous != array[i]:
			res += f"{count}{previous}"
			previous = array[i]
			count = 1
		i += 1
	res += f"{count}{previous}"
	return res

array = "aaaabbbccccddddd"
print(count(array))
