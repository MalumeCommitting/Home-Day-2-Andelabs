def words(string):
  
	w_occurrance = {}
	word_list = string.split()
	
	for word in word_list:
		if (word.isdigit()):
			word = int(word)
		if (word in w_occurrance):
			w_occurrance[word] = w_occurrance[word] + 1
		else:
			w_occurrance[word] = 1
	return w_occurrance
