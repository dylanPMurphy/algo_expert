

def maxSubsetSumNoAdjacent(array):
	if len(array) < 1:
        return 0
	if len(array) < 2:
		return array[0]
    maxSums = array[:]
    maxSums[1] = max(maxSums[0], maxSums[1])
    for i in range(2,len(array)):
            maxSums[i] = max(maxSums[i-1], maxSums[i-2]+array[i])
    return maxSums[len(maxSums)-1]