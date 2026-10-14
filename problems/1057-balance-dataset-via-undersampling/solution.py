from collections import Counter, defaultdict
def balance_undersample(data: list) -> list:
    """
    Undersample the majority classes so all classes have the same number of
    samples equal to the minority class count.

    data: list of (sample, label) tuples
    Returns: list of (sample, label) tuples, order-preserving
    """
    if not data :
        return []
    label_counts = Counter(row[1] for row in data)
    min_label,min_label_count = min(label_counts.items(),key= lambda x : x[1])
    balance_data = []
    balance_label_counts = defaultdict(int)
    for sample,label in data :
        if(balance_label_counts[label]+1<=min_label_count) :
            balance_data.append((sample,label))
            balance_label_counts[label]+=1
    return balance_data
    pass
