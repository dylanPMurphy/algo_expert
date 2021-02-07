def validIPAddresses(string):
	ipAddressesFound = []

	for i in range(1, min(len(string), 4)):
		currentIPAddressOctets = ['','','','']
		currentIPAddressOctets[0]= string[:i]
		if not isValidOctet(currentIPAddressOctets[0]):
			continue
		for j in range(i+1, i + min(len(string)-i, 4)):
			currentIPAddressOctets[1] = string[i:j]
			if not isValidOctet(currentIPAddressOctets[1]):
				continue
			for k in range(j+1,j+min(len(string)-j,4)):
				currentIPAddressOctets[2]= string[j:k]
				currentIPAddressOctets[3] = string[k:]
				if isValidOctet(currentIPAddressOctets[2]) and isValidOctet(currentIPAddressOctets[3]):
					ipAddressesFound.append('.'.join(currentIPAddressOctets))
	return ipAddressesFound
def isValidOctet(string):
	if int(string)>255:
		return False
	return len(string)==len(str(int(string))) #check for leading 0
