def sort_array(array):
    length = len(array)
    for i in xrange(0,length):
	for j in xrange(0,length-1):
	    if array[j] > array[j+1]:
	        array[j],array[j+1] = array[j+1],array[j]
    return array
