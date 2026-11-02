import math

def softmax(scores: list[float]) -> list[float]:
    # Your code here
    mini = max(scores)
    scores = [math.exp(score-mini) for score in scores]
    return [score/sum(scores) for score in scores]
    pass