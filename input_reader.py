from os import listdir
from os.path import isfile, join

def read_files():
	onlyfiles = ['input/'+f for f in listdir('input') if isfile(join('input', f))]

	lines = ''

	for file in onlyfiles:
		with open(file, 'r', encoding='utf-8') as f:
			lines += f.read()

	lines = lines.split('\n')
	
	return lines