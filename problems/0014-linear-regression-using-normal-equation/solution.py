import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	# Your code here, make sure to round
	x_np = np.array(X)
	x_transpose = x_np.T
	y_np = np.array(y)
	x_xt_inv = np.linalg.inv(x_transpose @ x_np)
	w = x_xt_inv @ x_transpose @ y
	return w