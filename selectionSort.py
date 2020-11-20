#Selection Sort
#Time Complexity O(n^2)
#Space complexity O(n)


def selectionSort(array):
    # Write your code here.
	currentIndex = 0
	
	while currentIndex < len(array) - 1:
		smallestIndex = currentIndex
		for i in range(currentIndex + 1,  len(array)):
			if array[smallestIndex]>array[i]:
				smallestIndex = i
		swap(currentIndex, smallestIndex, array)
		currentIndex += 1	
	return array
def swap(i,j,array):
	array[i], array[j] = array[j], array[i]



#>>>import selectionSort 
#>>> arr = [345,346,34567,2,34,235,675437,6,7,54,3,32,412,3,242,3,76,4,47,8,5,45,6,892347293847,1]
#>>> selectionSort.selectionSort(arr)
#[1, 2, 3, 3, 3, 4, 5, 6, 6, 7, 8, 32, 34, 45, 47, 54, 76, 235, 242, 345, 346, 412, 34567, 675437, 892347293847]