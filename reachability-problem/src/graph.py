import networkx as nx
import random
import matplotlib.pyplot as plt
from vertex import *


"""Class to represent a Graph"""
class Graph(object):


	"""
		name: the name of the graph
		V: the vertex set
		E: the edges set
	"""
	def __init__(self: object, name: str, V: list, E: list):
		self.name = name
		self.V = list()
		self.E = list(map(lambda x: tuple(x.split('-')), E))
		self.path = list() # The path to end vertex, since this algorithm is non-deterministic the path always changes between executions

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


	"""Function to show nice graph"""
	def show_graph(self: object, title: str):
		G = nx.Graph()
		G.add_nodes_from(list(map(lambda x: x.name, self.V)))
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
		pos = nx.shell_layout(G)
		nx.draw_networkx(G, pos=pos,with_labels=True, node_color='#00E8FC', edge_color=colors, width=1.0)
		plt.title(title)
		plt.axis("off")
		mng = plt.get_current_fig_manager()
		mng.canvas.set_window_title(self.name)
		plt.show()


	"""Auxiliary function to get the Vertex object given its name"""
	def to_vertex(self: object, name: str) -> Vertex:
		for vertex in self.V:
			if vertex.name == name:
				return vertex

	"""
		Function to solve the reachability problem in a non-deterministic way.
		init: the init vertex
		end_ the last vertex
	"""
	def solve_reachability(self: object, init: str, end: str) -> bool:
		self.path = list()
		edges = self.E
		reverse_edges = [edge[::-1] for edge in self.E]
		all_edges = edges + reverse_edges
		all_edges = list(set(all_edges))
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