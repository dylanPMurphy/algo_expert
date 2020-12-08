def bubbleSort(array):
    # Write your code here.
	
	swapped = True
	while(swapped):
		swapped = False
		runner = 1
		slow_runner = 0
		while(runner < len(array)):
			
			
			
			if array[runner] < array[slow_runner]:
				temp = array[runner]
				array[runner]=array[slow_runner]
				array[slow_runner] = temp
				swapped = True
			runner+=1
			slow_runner+=1
	return array
