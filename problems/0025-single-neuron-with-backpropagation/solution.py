import numpy as np
 
def sigmoid(x : np.ndarray) -> np.ndarray :
    return 1/(1+np.exp(-x))

def train_neuron(features: np.ndarray, labels: np.ndarray, initial_weights: np.ndarray, initial_bias: float, learning_rate: float, epochs: int) -> (np.ndarray, float, list[float]):
    # Your code here
    mse_values=[]
    updated_weights = initial_weights.copy()
    updated_bias = initial_bias
    n = len(labels)
    for _ in range(epochs) :
        logits =  features @ updated_weights + updated_bias
        probs = sigmoid(logits)
        mse_loss = np.mean(np.abs(labels-probs)**2)
        mse_values.append(round(mse_loss,4))
        error =  probs -labels
        delta = error * probs * (1-probs)
        dw = (2/n) * (features.T @ delta)
        db = 2/n * np.sum(delta)

        updated_weights -= learning_rate * dw
        updated_bias -= learning_rate * db


    return updated_weights, updated_bias, mse_values