import string


def setup_index():
	list_letters = list(string.ascii_lowercase)	
	letter_dict = {}
	index = 0

	for letter in list_letters:
		letter_dict[letter] = index
		index = index + 1
	return letter_dict


def generate(plain_file_path, cipher_file_path, rot_num):
	plain_file = open(plain_file_path, "r")
	cipher_file = open(cipher_file_path, "w+")

	lines = plain_file.readlines()

	for line in lines:
		cipher_line = ""
		line = line.strip()
		line = line.lower()

		for char in line:
			new_char = rotate(rot_num, char)
			cipher_line = cipher_line + new_char
		cipher_file.write(cipher_line + "\n")

	plain_file.close()
	cipher_file.close()


def rotate(rot_num, character):
	letter_dict = setup_index()
	index_dict = {v: k for k, v in letter_dict.items()}
	max_index = 26

	index = letter_dict.get(character)

	if index is not None:
		index = index + rot_num
		index = index % max_index

		return index_dict.get(index)
	else:
		return " "
