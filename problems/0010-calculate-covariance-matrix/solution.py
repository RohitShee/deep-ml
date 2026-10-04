import numpy as np
def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	# Your code here
	n = len(vectors)
	cov = [[0]*n for _ in range(n)]
	for x in range(n) :
		xbar = np.mean(vectors[x], axis=0)
		m = len(vectors[0])
		for y in range(n) :
			val =0
			ybar = np.mean(vectors[y],axis=0)
			for i in range(m) :
				val+=(vectors[x][i]-xbar)*(vectors[y][i]-ybar)
			val=val/(m-1)
			cov[x][y]=float(val)

	return cov