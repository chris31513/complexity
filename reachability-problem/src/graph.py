import networkx as nx
import random
import matplotlib.pyplot as plt
from vertex import *

class Graph(object):

	def __init__(self: object, name: str, V: list, E: list):
		self.name = name
		self.V = list()
		self.v = V
		self.e = list(map(lambda x: tuple(x.split('-')), E))
		self.E = list()
		self.path = list()

		for v in V:
			vertex = Vertex(v)
			self.V.append(vertex)

		for edge in E:
			pair = edge.split('-')

			for v in self.V:
				if pair[0] == v.name:
					for v1 in self.V:
						if pair[1] == v1.name:
							v.set_neighbor(v1)
				elif pair[1] == v.name:
					for v1 in self.V:
						if pair[0] == v1.name:
							v.set_neighbor(v1)

	def show_graph(self: object, title: str):
		G = nx.Graph()
		G.add_nodes_from(self.v)
		path_to_edges = list()

		for i in range(0, len(self.path) - 1):
			path_to_edges.append((self.path[i].name, self.path[i+1].name))
			path_to_edges.append((self.path[i+1].name, self.path[i].name))


		for edge in self.e:
			if edge in path_to_edges:
				G.add_edge(*edge,color='r',weight=2)
			else:
				G.add_edge(*edge,color='#000000',weight=2)

		edges = G.edges()
		colors = [G[u][v]['color'] for u,v in edges]
		pos = nx.spring_layout(G)
		nx.draw_networkx(G, pos=pos,with_labels=True, node_color='#00E8FC', edge_color=colors, width=1.0)
		plt.title(title)
		plt.axis("off")
		plt.show()

	def solve_reachability(self: object, init: str, end: str) -> bool:
		self.path = list()

		for vertex in self.V:
			if vertex.name == init:
				random_vertex = vertex

		while not random_vertex in self.path:
			self.path.append(random_vertex)
			if random_vertex.name == end:
				break
			random_vertex = random.choice(random_vertex.neighbors)

		return self.path[len(self.path) - 1].name == end