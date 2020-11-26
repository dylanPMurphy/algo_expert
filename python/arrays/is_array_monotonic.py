def isMonotonic(array):
    # Write your code here
	trend = 0
	for i in range(0, len(array)-1):
		
		if array[i]==array[i+1]:
			pass
		elif array[i]>array[i+1]:
			if trend == 0:
				trend = -1
			elif trend == -1:
				pass
			elif trend == 1:
				return False
		elif array[i]<array[i+1]:
			if trend == 0:
				trend = 1
			elif trend == 1:
				pass
			elif trend == -1:
				return False
	return True