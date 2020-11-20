#Insertion Sort
#Time Complexity O(n^2)
#Space complexity O(n)


def insertionSort(array):
    # Write your code here.
	for i in range(1, len(array)):
		j = i
		while j > 0 and array[j] < array[j-1]:
			swap(j, j-1, array)
			j -= 1
	return array
		
def swap(i, j, array):
	array[i], array[j] = array[j], array[i]
#>>> import insertionSort
#>>> arr = [54,3,235,46,34567,4567,23,12,3,5,6,77,4,32,75685,901]
#>>> print(insertionSort.insertionSort(arr))
#[3, 3, 4, 5, 6, 12, 23, 32, 46, 54, 77, 235, 901, 4567, 34567, 75685] 

