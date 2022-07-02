arr = [1, 10, 23, 7, 10, 3, 3, 90]
arr_dict = {}

dup = []
for i in arr:
	if i not in arr_dict:
		arr_dict[i] = 1
	else:
		dup.append(i)
print(dup)


# for value in arr:
#  	arr_dict[value] = arr_dict.get(value, 0) + 1

# print(arr_dict)


input_string = "HELLO WORLD!"
convert_lower = lambda string: string[:len(input_string)].lower()

print(convert_lower(input_string))

print(bool(10) == True)