import json
import os
import sys
from graph import *


"""
	Function that reads a file in data/ and builds the graph.

	Note: all files for this algorithm should be written like this: {Name: graph_name, V: vertex_list, E: edges_set}

	The edge's description should be like this: 'vn-vm' with vn and vm in V and vm != vn.

	I assume the graph isn't directed, so if 'vn-vm' is in E I automatically add 'vm-vn' to E. So it isn't necessary to put 'vn-vm' and 'vm-vn' in the description of E.

"""
def parse_graph(file: str) -> Graph:

	with open(os.path.dirname(__file__) + '/../data/' + file, 'r') as loaded:
		description = loaded.read().replace("'", '')
		important_data = {0: 'Name', 1: 'V', 2: 'E'}
		splited_description = list(map(lambda x: x.replace(',V', '') if ',V' in x else x.replace(',E', '') if ',E' in x else x,list(filter(lambda x: x != 'Name', description.replace('{', '').replace('}', '').replace(' ', '').split(':')))))
		rebuilded_description = list()
		for data in splited_description:
			if '[' in data:
				raw = data.replace('[', '').replace(']', '').split(',')
				valid = '"' + important_data[splited_description.index(data)] + '":' + '["' + raw[0] + '"'

				for item in raw[1:]:
					valid += ',"' + item + '"'

				valid += ']'
				rebuilded_description.append(valid)

			else:
				rebuilded_description.append('"' + important_data[splited_description.index(data)] + '":' + '"' + data + '"')

		rebuilded_graph = '{' + ','.join(rebuilded_description) + '}'
		json_graph = json.loads(rebuilded_graph)

		return Graph(json_graph['Name'], json_graph['V'], json_graph['E'])

if __name__ == '__main__':
	file = sys.argv[1]
	init = sys.argv[2]
	end = sys.argv[3]
	graph = parse_graph(file)
	is_reachable = graph.solve_reachability(init, end)

	if is_reachable:
		graph.show_graph('Sí se encontró un camino')
	else:
		graph.show_graph('No se encontró un camino')