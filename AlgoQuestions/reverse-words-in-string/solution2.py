# time : O(n) | space : O(n)
def reverseWordsInString(string):
	words = []
	startOfWords = 0

	for idx in range(len(string)):
		character = string[idx]
		
		if character == " ":
			words.append(string[startOfWords:idx])
			startOfWords = idx

		elif string[startOfWords] == " ":
			words.append(" ")
			startOfWords = idx

	words.append(string[startOfWords:])

	reverse_list(words)
	return "".join(words)

def reverse_list(words):
	start, end = 0, len(words)-1

	while start < end:
		words[start], words[end] = words[end], words[start]
		start += 1
		end -= 1

string =  "AlgoExpert is the best!"
print(reverseWordsInString(string))
