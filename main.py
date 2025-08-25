import os
import sys

import rot
#Setup argparse (I'm lazy)

def main(working_dir, cipher):
	text_path = working_dir + "/plain.txt"
	file_exists = os.path.exists(text_path)

	if (file_exists):
		generate(cipher, text_path)
	else:
		print("No plaintext file found at: " + text_path)
		

def generate(cipher, text_path):		
	#add multiple types of ciphers, just hardcoded for now
	if(cipher != "rot13"):
		print("Unsupported cipher type")
		sys.exit()

	letter_dict = rot.setup_index()
	print(letter_dict)
		

if __name__ == "__main__":
	working_dir = os.path.dirname(os.path.realpath(__file__))
	main(working_dir, "rot13")
