def reverseWordsInString(string):
	words = []
	startOfWord = 0
	for i in range(0,len(string)):
		character = string[i]
		
		if character == " ":
			words.append(string[startOfWord:i])
			startOfWord = i
		elif string[startOfWord] == " ":
			words.append(" ")
			startOfWord = i

	words.append(string[startOfWord:])
	reverseList(words)
	return ''.join(words)


def reverseList(list):
	start = 0
	end = len(list)-1
	while start < end:
		list[start], list[end] = list[end], list[start]
		start+=1
		end -=1
