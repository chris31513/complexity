import networkx as nx
import random
import matplotlib.pyplot as plt
from vertex import *

class Graph(object):

	def __init__(self: object, name: str, V: list, E: list):
		self.name = name
		self.V = list()
		self.v = V
		self.E = list(map(lambda x: tuple(x.split('-')), E))
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


		for edge in self.E:
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

	def to_vertex(self: object, name: str) -> Vertex:
		for vertex in self.V:
			if vertex.name == name:
				return vertex

	def solve_reachability(self: object, init: str, end: str) -> bool:
		self.path = list()
		edges = self.E
		reverse_edges = [edge[::-1] for edge in self.E]
		all_edges = edges + reverse_edges
		self.path.append(self.to_vertex(init))

		while set(self.V) != set(self.path):
			last_added = self.path[len(self.path) - 1]
			previous_last_added = None

			if len(self.path) != 1:
				previous_last_added = self.path[len(self.path) - 2]

			reachable_vertices = list(set([edge[0] if edge[1] == last_added.name else edge[1] for edge in list(filter(lambda v: v != None, [edge if edge[0] == last_added.name else None for edge in all_edges]))]))
			
			if len(reachable_vertices) == 0:

				break

			else:

				random_vertex_name = random.choice(reachable_vertices)

				if len(reachable_vertices) != 1 and previous_last_added != None and random_vertex_name == previous_last_added.name:

					random_vertex_name = random.choice(list(filter(lambda v: v != previous_last_added.name, reachable_vertices)))


				random_vertex = self.to_vertex(random_vertex_name)
				self.path.append(random_vertex)

				if random_vertex_name == end:
					break

				all_edges = list(filter(lambda edge: edge != (last_added.name, random_vertex_name), all_edges))


		return self.path[len(self.path) - 1].name == end