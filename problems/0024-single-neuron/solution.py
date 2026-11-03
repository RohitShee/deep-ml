import math

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	# Your code here
	probabilities=[]
	mse =0
	sample_size = len(features)
	for feature,label in zip(features,labels) :
		op = 0;
		for f,w in zip(feature,weights) :
			op+=f*w
		op+=bias
		op = 1/(1+math.exp(-op))
		op = round(op,4)
		probabilities.append(op)
		mse+=(label-op)**2
	mse/=sample_size
	return probabilities, round(mse,4)