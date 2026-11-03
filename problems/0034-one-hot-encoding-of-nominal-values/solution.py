import numpy as np

def to_categorical(x, n_col=None):
	# Your code here
	sample_size = len(x)
	if n_col is None :
		n_col =len(set(x))
	one_hot_encoding = np.zeros((sample_size,n_col))
	for idx,val in enumerate(x) :
		one_hot_encoding[idx][val]=1
	return one_hot_encoding
	pass