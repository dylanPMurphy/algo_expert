def isPalindrome(string):
    for i in range(0, len(string)//2):
		reverse_index = len(string)-1-i
		if string[i] != string[reverse_index]:
			return False
	return True
