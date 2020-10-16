import os
import sys
import random

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

	instance = '{%s,%s,%s}' % ('Name:'+name, 'V:'+str(vertices), 'E:'+str(edges))
	file = open(os.path.dirname(__file__) + '/../data/' + name + '.rp', 'w+')
	file.write(instance)

if __name__ == '__main__':
	build(sys.argv[1], int(sys.argv[2]))