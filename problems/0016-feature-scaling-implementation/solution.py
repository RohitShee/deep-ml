import numpy as np

def standarization(data : np.ndarray) -> (np.ndarray) :
	mean,std = np.mean(data, axis=0), np.std(data, axis=0)
	return np.array([(x-mean)/std for x in data])

def min_max_normalization(data : np.ndarray) -> (np.ndarray) :
	mini,maxi = np.min(data, axis=0), np.max(data, axis=0)
	return np.array([(x-mini)/(maxi-mini) for x in data])

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	# Your code here
	return standarization(data), min_max_normalization(data)