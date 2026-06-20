def min_max(x: list[float]) -> list[float]:
    """
    Perform Min-Max normalization to scale values to [0, 1].
    
    Args:
        x: A list of numerical values
    
    Returns:
        A new list with values normalized to [0, 1]
    """
    # Your code here
    maxi = max(x)
    mini = min(x)
    ans=[]
    for num in x :
        ans.append((num-mini)/(maxi-mini))
    return ans
    pass