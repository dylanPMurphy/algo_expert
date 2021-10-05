def kadanesAlgorithm(array):
    max_sum = array[0]
    max_ending_here = array[0]
    for num in array[1:]:
        max_ending_here = max(num, max_ending_here+num)
        max_sum= max(max_sum, max_ending_here)
    return max_sum