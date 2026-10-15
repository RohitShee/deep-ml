import numpy as np
from typing import List, Tuple

def k_fold_cross_validation(n_samples: int, k: int = 5, shuffle: bool = True) -> List[Tuple[List[int], List[int]]]:
    """
    Generate train/test index splits for k-fold cross-validation.
    
    Args:
        n_samples: Total number of samples in the dataset
        k: Number of folds (default 5)
        shuffle: Whether to shuffle indices before splitting (default True)
    
    Returns:
        List of (train_indices, test_indices) tuples
    """
    indexes = np.arange(n_samples)
    if shuffle :
        np.random.shuffle(indexes)
    cv = []
    fold_size = [n_samples//k]*k
    fold_size[0] += n_samples%k
    start_idx= 0
    for i in range(k) :
        cv.append((np.concatenate((indexes[0: start_idx],indexes[start_idx+fold_size[i] : n_samples])),indexes[start_idx : start_idx+fold_size[i]]))
        start_idx+=fold_size[i]
    return cv
    # Your code here
    pass