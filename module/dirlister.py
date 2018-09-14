import os
def run(**args):
	print("[*] W module dirlist")
	files =os.listdir(".")
	return str(files)