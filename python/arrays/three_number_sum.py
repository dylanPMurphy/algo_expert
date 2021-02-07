#First we will sort the array
def threeNumberSum(array, targetSum):
	
	sorted_array = array.sort()
	triplets = []
	
	for i in range(0,len(array)-2):	
		current_sum = 0
		current_index = i
		left = i+1
		right = len(array)-1
		while left < right:
			currentSum = array[i] + array[left] + array[right]
			if currentSum == targetSum:
				triplets.append([array[i], array[left], array[right]])
				left +=1
				right -=1
			elif currentSum < targetSum:
				left += 1
			elif currentSum > targetSum:
				right -= 1
	return triplets
