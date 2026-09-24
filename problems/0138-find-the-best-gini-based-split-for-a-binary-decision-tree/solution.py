import numpy as np
from typing import Tuple

def gini(x : np.ndarray) -> float :
    zero = sum(y==0 for y in x)
    one = sum(y==1 for y in x)
    total = zero+one
    s_zero= zero/total
    s_one =one/total
    return 1.0 - (s_zero**2+s_one**2)
    

def find_best_split(X: np.ndarray, y: np.ndarray) -> Tuple[int, float]:
    """Return the (feature_index, threshold) that minimises weighted Gini impurity."""
    # ✏️ TODO: implement
    n_features = len(X[0])
    n_samples = len(y)
    best_feature = None
    best_threshold = None
    best_gain = -1.0
    impurity_node = gini(y)
    for idx in range(n_features) :
        values = sorted(set(X[i][idx] for i in range(n_samples)))
        if len(values) <=1 :
            continue
        for i in range (len(values)-1) :
            threshold = values[i]
            left_y = [y[j] for j in range(len(X)) if X[j][idx] <= threshold]
            right_y = [y[j] for j in range(len(X)) if X[j][idx] > threshold]
            impurity_left = gini(left_y)
            impurity_right = gini(right_y)
            gain = impurity_node -(len(left_y)/len(X)*impurity_left+len(right_y)/len(X)*impurity_right)
            if gain > best_gain  :
                best_gain = gain
                best_feature= idx
                best_threshold=threshold
    return (best_feature,best_threshold)

    pass