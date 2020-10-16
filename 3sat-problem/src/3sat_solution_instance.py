import numpy as np
import os
import sys
import random

"""3SAT-Problem instance for solution"""
class SAT_INSTANCE(object):
	
	"""
	   n_v: number of variables
	   n_c: number of clauses
	   clauses: logic formule joined with and
	"""
	def __init__(self: object, n_v: int, n_c: int, clauses: list):
		self.n_v = n_v
		self.n_c = n_c
		self.clauses = clauses
		trues = [np.ones(shape=(len(x)), dtype=bool).tolist() for x in self.clauses] # Array of trues
		pairs = list() # List for build the pairs (Variable, Boolean)
		self.solution = list() # First solution, all variables are True considering the negated variables

		for i in range(0, n_c):
			pairs.append(list(zip(clauses[i], trues[i])))

		for value in pairs:

			for x in value:

				"""Ignore pairs already added and avoiding inconsistencies with negated variables"""

				if not x in self.solution:
					if not (x[0], not x[1]) in self.solution:
						if (x[0]*(-1), x[1]) in self.solution:
							self.solution.append((x[0], not x[1]))
						else:
							self.solution.append(x)

		self.solution_size = len(self.solution) # Size of the solution for the random solution
		self.satisfied_clauses = 0
		self.satisfies = False # Variable to know if the solution satisfies the clauses, False at start

	"""Function to print the instance"""
	def __str__(self: object) -> str:
		seed = 'Seed: ' + str(np.random.get_state()[1][0]) + '\n'
		Nv = 'Nv: ' + str(self.n_v) + '\n'
		Nc = 'Nc: ' + str(self.n_c) + '\n'
		binary_vector = 'Binary Vector: ' + str(self.binary_vector) + '\n'
		satisfied_clauses = 'Satisfied clauses: {} of {}\n'.format(self.satisfied_clauses, self.n_c)
		is_sat = ''
		if self.satisfies:
			is_sat = 'Satisfies: ' + '\033[92m' + str(self.satisfies)
		else:
			is_sat = 'Satisfies: ' + '\033[91m' + str(self.satisfies)
		return seed+Nv+Nc+binary_vector+satisfied_clauses+is_sat

	"""Create random pairs (Variable, Boolean)"""
	def create_random_solution(self: object):
		random_booleans = list(map(lambda x: True if x==1 else False, np.random.randint(low=0, high=2, size=(self.solution_size)).tolist())) # Array of random booleans
		pairs = [(x[0][0], x[1]) for x in zip(self.solution, random_booleans)] # Assign boolean values
		random_solution = list()

		"""Avoid inconsistencies"""
		for x in pairs:
			if (x[0]*(-1), x[1]) in random_solution:
				random_solution.append((x[0], not x[1]))
			else:
				random_solution.append(x)

		self.binary_vector = list(map(lambda x: 1 if x else 0, random_booleans))
		self.solution = random_solution

	"""Return the boolean value of a variable"""
	def get_boolean_value(self: object, variable: int) -> bool:

		for pair in self.solution:
			if pair[0] == variable:
				return pair[1]

		raise Exception('VariableNotInSolution') # If variable not in first solution

	"""Evaluate the random solution"""
	def evaluate_solution(self: object):
		formule = True

		for clause in self.clauses:

			boolean_clause = False

			for variable in clause:
				boolean_clause = boolean_clause or (self.get_boolean_value(variable))

			if boolean_clause:
				self.satisfied_clauses = self.satisfied_clauses + 1

			formule = formule and boolean_clause

		self.satisfies = formule

"""Reads the definition in a .txt file and builds a 3sat instance"""
def parse_instance(instance: str) -> SAT_INSTANCE:
	with open(instance, 'r') as file:
		parts = file.read().split('\n')
		n_v = int(parts[0])
		n_c = int(parts[1])
		pre_clauses = list(filter(lambda x: x != '', parts[2:]))
		pre_clauses = list(map(lambda x: x.split(' '), pre_clauses))
		clauses = [list(map(lambda x: int(x), pre_clauses[i])) for i in range(0, n_c)]
		return SAT_INSTANCE(n_v, n_c, clauses)

if __name__ == '__main__':
	sat_instance = parse_instance(os.path.dirname(__file__) + '/../data/' + sys.argv[1])
	sat_instance.create_random_solution()
	sat_instance.evaluate_solution()
	print(sat_instance)