def find_max_min(numbers): """passed numbers as an argument that will
							  later be the list that the 'if' will be using"""
	numbers is list
	if(len(numbers) > 1): # There has to be atleast two items in the list for comparison of the min() max()
	    if(max(numbers) == min(numbers)):
	    	return [len(numbers)]
	    else:
	    	return [min(numbers), max(numbers)]