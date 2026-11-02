import math

def softmax(scores: list[float]) -> list[float]:
    # Your code here
    maxi = max(scores)
    scores = [math.exp(score-maxi) for score in scores]
    return [score/sum(scores) for score in scores]
    pass