# time : O(n) | space : O(n)
def reverseWordsInString(string):
	characters = [char for char in string]
	reverse_list_Range(characters, 0, len(characters) - 1)

	start_word = 0
	while start_word < len(characters):
		endOfWord = start_word
		while endOfWord < len(characters) and characters[endOfWord] != " ":
			endOfWord += 1

		reverse_list_Range(characters, start_word, endOfWord - 1)
		start_word = endOfWord + 1

	return "".join(characters)


def reverse_list_Range(list, start, end):
	while start < end:
		list[start], list[end] = list[end], list[start]
		start += 1
		end -= 1


string =  "AlgoExpert is the best!"
print(reverseWordsInString(string))