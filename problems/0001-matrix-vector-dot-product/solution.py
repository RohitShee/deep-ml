import numpy as np
def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	dot_products=[]
	m = len(b)
	for vector in a :
		if len(vector) != m :
			dot_products.append(-1)
		else :
			dot_products.append(np.dot(vector, b))
	return dot_products
	pass