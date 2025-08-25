import string


def setup_index():
	list_letters = list(string.ascii_lowercase)	
	letter_dict = {}
	index = 0

	for letter in list_letters:
		letter_dict[letter] = index
		index = index + 1
	return letter_dict
