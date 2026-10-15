import numpy as np

def shuffle_data(X, y, seed=None):
	# Your code here
	np.random.seed(seed)
	indexes = np.arange(len(y))
	np.random.shuffle(indexes)
	X = X[indexes]
	y = y[indexes]
	return X,y
	pass