import re
from stopwords import allStopWords

def map(value, context):

	parts = value.split(':::')

	if(len(parts) != 3):
		return

	authors = parts[1].split('::')
	words = parts[2].split(' ')

	word_count = {}
	for word in words:
		w = re.sub('[^A-Za-z0-9]+', '', word).lower()
		
		if w not in allStopWords.keys():
			if w not in word_count.keys():
				word_count[w] = 1
			else:
				word_count[w] += 1

	for author in authors:
		if author not in context.keys():
			context[author] = []
		
		context[author].append(word_count)
		