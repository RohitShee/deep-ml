import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	n = len(a)
	m = len(a[0])
	if n*m!=new_shape[0]*new_shape[1] :
		return []
	c = [element for sublist in a for element in sublist ]
	reshaped_matrix = [[] for _ in range(new_shape[0])]
	for i in range(new_shape[0]) :
		reshaped_matrix[i]=c[i*new_shape[1] : (i+1)*new_shape[1]]
	return reshaped_matrix