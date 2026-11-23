import numpy as np

def tanh(x) :
    return (np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x))

def rnn_forward(input_sequence: list[list[float]], initial_hidden_state: list[float], Wx: list[list[float]], Wh: list[list[float]], b: list[float]) -> list[float]:
    input_sequence = np.array(input_sequence)
    hidden_state = np.array(initial_hidden_state)
    Wx = np.array(Wx)
    Wh = np.array(Wh)
    b = np.array(b)
    for t in range(len(input_sequence)) :
        hidden_state = tanh(Wx @ input_sequence[t] + Wh @ hidden_state + b)
    return np.round(hidden_state,4)