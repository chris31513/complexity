class Vertex(object):

	def __init__(self: object, name: str, neighbors: list = None):
		self.name = name
		if neighbors == None:
			self.neighbors = list()
		else:
			self.neighbors = neighbors

	def __str__(self: object) -> str:
		name = '(Name: ' + self.name + ', ' 
		neighbors = 'Neighbors: ' + '[' + ', '.join(list(map(lambda x: x.name, self.neighbors))) + '])'
		return name + neighbors

	def set_neighbor(self: object, vertex: object):
		self.neighbors.append(vertex)


	def is_neighbor(self: object, vertex: object) -> bool:
		return vertex in self.neighbors