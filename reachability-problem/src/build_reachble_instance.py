import os
import sys
import random
import math


"""Function tu build a graph for the reachability problem using the description of a graph."""
def build(name: str, size: int):
	vertices = list(map(lambda x: 'v'+str(x), list(range(1, size+1))))
	counted_vertices = list()
	edges = list()
	
	while set(counted_vertices) != set(vertices):
		v1 = random.choice(vertices)
		v2 = random.choice(vertices)
		if v1 != v2:
			edge = v1 + '-' + v2
			reverse_edge = v2 + '-' + v1
			if not edge in edges:
				if not reverse_edge in edges:
					edges.append(edge)
		else:
			continue

		if not v1 in counted_vertices:
			counted_vertices.append(v1)

	final_edges = list()
	random.shuffle(edges) 
	i = 0

	while len(final_edges) != math.ceil(len(edges)/2): # I remove random edges to make the instance more random
		final_edges.append(edges[i])
		i += 1

	instance = '{%s,%s,%s}' % ('Name:'+name, 'V:'+str(vertices), 'E:'+str(final_edges))
	file = open(os.path.dirname(__file__) + '/../data/' + name + '.rp', 'w+')
	file.write(instance)

if __name__ == '__main__':
	build(sys.argv[1], int(sys.argv[2]))