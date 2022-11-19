# key: nome do author
# result_list: dicionarios com a contagem das palavras

def reduce(key, result_list):
	
	word_count_list = {}

	for result in result_list:
		for word_key in result.keys():
			if word_key not in word_count_list.keys():
				word_count_list[word_key] = 0
			
			word_count_list[word_key] += result[word_key]

	result = f"{key} | "

	for word in word_count_list.keys():
		result += f"{word}: {word_count_list[word]}, "

	result += '\n'

	return result