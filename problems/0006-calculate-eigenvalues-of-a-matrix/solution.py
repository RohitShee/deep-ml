import math
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	
	add = math.sqrt((matrix[0][0]-matrix[1][1])**2+4*matrix[0][1]*matrix[1][0])
	eigenvalues = [matrix[0][0]+matrix[1][1]+add,matrix[0][0]+matrix[1][1]-add]
	eigenvalues = [0.5*val for val in eigenvalues]
	return eigenvalues