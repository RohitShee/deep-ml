import numpy as np

def calculate_auc(y_true, y_scores):
    """
    Calculate the Area Under the ROC Curve (AUC).
    
    Args:
        y_true: List or array of binary ground truth labels (0 or 1)
        y_scores: List or array of predicted probabilities or confidence scores
        
    Returns:
        AUC value as a float
    """

    n = len(y_true)
    sorted_idx = np.argsort(y_scores)[::-1]
    y_scores_sorted = [y_scores[i] for i in sorted_idx]
    y_true_sorted = [y_true[i] for i in sorted_idx]

    pre_positive_count=np.cumsum(y_true_sorted, axis=0)
    
    TPR,FPR = [],[]

    for i in range(n) :
        threshold = y_scores_sorted[i]
        TP,FP = pre_positive_count[i],i+1-pre_positive_count[i]
        TN,FN = n-i-1-pre_positive_count[n-1]+pre_positive_count[i],pre_positive_count[n-1]-pre_positive_count[i]

        if TP+FN == 0 :
            TPR.append(0)
        else :
            TPR.append(TP/(TP+FN))
        if TN+FP == 0 :
            FPR.append(0)
        else :
            FPR.append(FP/(TN+FP))
        #print(TPR[i],FPR[i])
    
    AUC = 0
    for i in range(1,n) :
        AUC+=(TPR[i]+TPR[i-1])/2*(FPR[i]-FPR[i-1])
    
    return AUC
    
    pass