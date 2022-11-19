# Lendo todos os arquivos
from input_reader import read_files
lines = read_files()

# Iniciando MapReduce
from map import map
from reduce import reduce

# Variaveis para guardar os resultados
map_results = {}
reduce_results = ''

# Fase de Map
for line in lines:
	map(line, map_results)

# Fase de Reduce
for author in map_results.keys():
	reduce_results += reduce(author, map_results[author])

# Salvando resultado no arquivo de texto
with open('output/result.txt', 'w', encoding='utf-8') as w:
	w.write(reduce_results)
	