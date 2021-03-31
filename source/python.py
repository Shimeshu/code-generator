'''
Generates a Python Project
'''

import os


def createProject(name):
	os.mkdir(name)
	f = open(f"{name}/Main.py", "w+")
	code = '''# Auto - Generated Code

def main():
	return "Hello World"

if __name__ == '__main__':
	print(main())

	'''
	f.write(code)
	readme = open(f"{name}/Readme.txt", "w+")
	readme.write("Write your Readme Here")
	readme.close()
	license = open(f"{name}/License.txt", "w+")
	lic_text = open("source/license.txt", "r+")
	text = lic_text.read()
	license.write(text)
	license.close()
	lic_text.close()
