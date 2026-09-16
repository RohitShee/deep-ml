import numpy as np

def numerical_gradient_check(f, x, analytical_grad, epsilon=1e-7):
    """
    Perform numerical gradient checking using centered finite differences.
    
    Args:
        f: A function that takes a numpy array and returns a scalar
        x: numpy array, the point at which to check gradient
        analytical_grad: numpy array, the analytically computed gradient
        epsilon: float, small value for finite difference approximation
    
    Returns:
        tuple: (numerical_grad, relative_error)
    """
    # Your code here
    h = epsilon
    num_grad = []
    for _ in range(len(x)):
        a = x.copy()
        b = x.copy()
        a[_]+=h
        b[_]-=h
        grad = (f(a)-f(b))/(2*h)
        num_grad.append(grad)
    numerator = np.linalg.norm(num_grad-analytical_grad)
    denominator = np.linalg.norm(num_grad)+np.linalg.norm(analytical_grad)
    rel_error = 0
    if denominator >0 :
        rel_error = numerator/denominator
    return (num_grad,rel_error)
    pass