import numpy as np
def sigmoid(x) :
    return 1/(1+np.exp(-x))
def tanh(x) :
    return (np.exp(x) - np.exp(-x))/(np.exp(x)+np.exp(-x))
class LSTM:
    def __init__(self, input_size, hidden_size):
        self.input_size = input_size
        self.hidden_size = hidden_size

        # Initialize weights and biases
        self.Wf = np.random.randn(hidden_size, input_size + hidden_size)
        self.Wi = np.random.randn(hidden_size, input_size + hidden_size)
        self.Wc = np.random.randn(hidden_size, input_size + hidden_size)
        self.Wo = np.random.randn(hidden_size, input_size + hidden_size)

        self.bf = np.zeros((hidden_size, 1))
        self.bi = np.zeros((hidden_size, 1))
        self.bc = np.zeros((hidden_size, 1))
        self.bo = np.zeros((hidden_size, 1))

    def forward(self, x, initial_hidden_state, initial_cell_state):
        """
        Processes a sequence of inputs and returns the hidden states, final hidden state, and final cell state.
        """
        h = initial_hidden_state
        c  = initial_cell_state
        hidden_states = []
        for xi in x : 
            data = np.vstack((h,xi.reshape(-1,1)))
            ft = sigmoid((self.Wf @ data)+self.bf)
            it = sigmoid((self.Wi @ data)+self.bi)
            ct = tanh((self.Wc @ data)+self.bc)
            c = ft*c + it*ct
            ot = sigmoid((self.Wo @ data)+self.bo)
            h = ot*tanh(c)
            hidden_states.append(h)
        return hidden_states, h, c
