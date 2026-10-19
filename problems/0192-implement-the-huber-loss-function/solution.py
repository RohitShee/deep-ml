def huber_loss(y_true, y_pred, delta=1.0):
	"""
	Compute the Huber Loss between true and predicted values.

	Args:
		y_true (float | list[float]): Ground truth values
		y_pred (float | list[float]): Predicted values
		delta (float): Transition threshold between MSE and MAE behavior

	Returns:
		float: Average Huber loss
	"""
	# Your code here
	if isinstance(y_true, float):
		if abs(y_true-y_pred)<=delta :
			return ((y_true-y_pred) ** 2) /2
		else :
			return delta(abs(y_true-y_pred)-delta/2)
	huber_loss=0.0
	for y,y_cap in zip(y_true,y_pred) :
		if abs(y-y_cap) <= delta :
		 	huber_loss += ((y-y_cap) ** 2) /2
		else :
			huber_loss += delta*(abs(y-y_cap)-delta/2)
	avg_huber_loss = huber_loss/len(y_true)
	return round(avg_huber_loss,4)
	pass