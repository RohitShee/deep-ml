import numpy as np

def compute_qkv(X, W_q, W_k, W_v):
    """Compute Query, Key, Value matrices from input X and weight matrices."""
    Q = np.dot(X, W_q)
    K = np.dot(X, W_k)
    V = np.dot(X, W_v)
    return Q, K, V

def softmax(x, axis=-1):
    """Row-wise softmax (softmax along the last axis by default)."""
    shifted = x - np.max(x, axis=axis, keepdims=True)  
    exp = np.exp(shifted)
    return exp / np.sum(exp, axis=axis, keepdims=True)

def self_attention(Q, K, V):
    """
    Compute scaled dot-product self-attention.
    
    Args:
        Q: Query matrix of shape (seq_len, d_k)
        K: Key matrix of shape (seq_len, d_k)
        V: Value matrix of shape (seq_len, d_v)
    
    Returns:
        Attention output of shape (seq_len, d_v)
    """
    attention_score = Q @ K.T /np.sqrt(Q.shape[1])
    A = softmax(attention_score)
    output = A @ V
    return output

    # Your code here
    pass
