import numpy as np

def log_softmax(scores: np.ndarray) -> np.ndarray:
    maxi = max(scores)
    log_sum = np.log(sum(np.exp(scores-maxi)))
    return [score-maxi-log_sum for score in scores]
