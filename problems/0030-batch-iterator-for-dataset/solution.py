import numpy as np

def batch_iterator(X, y=None, batch_size=64):
	# Your code here
	batches= []
	start =0;
	n_sample = len(X)
	while start<n_sample :
		X_batch = X[start : min(start+batch_size,n_sample), :]
		batch = X_batch
		if y is not None :
			batch = [X_batch,y[start : start+batch_size]]
		batches.append(batch)
		start+=batch_size
	return batches
	pass