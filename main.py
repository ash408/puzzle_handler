import os
import sys

import rot
#Setup argparse (I'm lazy)

def main(working_dir, cipher):
	text_path = working_dir + "/plain.txt"
	cipher_path = working_dir + "/cipher.txt"
	file_exists = os.path.exists(text_path)

	if (file_exists):
		#hardcoded cipher type for now
		rot.generate(text_path, cipher_path, 13)
	else:
		print("No plaintext file found at: " + text_path)
		

if __name__ == "__main__":
	working_dir = os.path.dirname(os.path.realpath(__file__))
	main(working_dir, "rot13")
