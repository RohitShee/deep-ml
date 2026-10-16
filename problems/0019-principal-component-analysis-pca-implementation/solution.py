import numpy as np

def pca(data: np.ndarray, k: int) -> np.ndarray:
    """
    Perform PCA and return the top k principal components.
    
    Args:
        data: Input array of shape (n_samples, n_features)
        k: Number of principal components to return
    
    Returns:
        Principal components of shape (n_features, k), rounded to 4 decimals.
        Each eigenvector's sign is fixed so its first non-zero element is positive.
    """
    # Your code here
    n_sample , n_feature = len(data), len(data[0])
    means = np.mean(data, axis=0)
    stds = np.std(data, axis=0)
    standarized_data = np.zeros((n_sample,n_feature))
    for j in range(n_feature) :
        for i in range(n_sample) :
            standarized_data[i][j] = (data[i][j]-means[j]) / stds[j]
    cov = np.cov(standarized_data, rowvar = False)
    eigenvalues,eigenvectors= np.linalg.eigh(cov)
    
    eigenvectors = eigenvectors[:, :: -1]
    
    PCA = eigenvectors[:,:k]
    for i in range(k) :
        vector = PCA[: , i]
        positive = True
        for x in vector :
            if abs(x) >1e-10 :
                if(x<0) :
                    positive = False
                break
        if not positive :
            PCA[: , i] = -vector
    return np.round(PCA,4)

    pass
