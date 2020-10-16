import numpy as np
import os
import sys
import random

if __name__ == '__main__':
	variables = int(sys.argv[1])
	clausulas = int(sys.argv[2])
	name = str(sys.argv[3])
	formulas = list()

	for i in range(0, clausulas):
		formulas.append(' '.join(list(map(lambda x: str(x), np.random.randint(low=(variables*(-1)), high=(variables+1), size=(3)).tolist()))))

	f = open(os.path.dirname(__file__) + '/../data/' + name, 'w+')
	f.write(str(variables)+'\n')
	f.write(str(clausulas)+'\n')
	
	for s in formulas:
		f.write(s+'\n')

	f.close()