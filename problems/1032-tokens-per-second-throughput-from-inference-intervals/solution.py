def compute_throughput(intervals):
    """
    Compute step-wise, cumulative, and overall tokens-per-second.

    Args:
        intervals: list of (tokens_processed, elapsed_seconds) tuples.

    Returns:
        dict with keys 'step_tps', 'cumulative_tps', 'overall_tps'.
    """
    step_tps=[]
    cumulative_tps=[]
    if len(intervals) == 0 :
        return {
            'step_tps' : step_tps,'cumulative_tps' : cumulative_tps,'overall_tps' : 0.0
        }
    token_count=0.0
    time_count = 0.0
    for token,time in intervals :
        if time<=0.0 or token<0 :
            raise ValueError("Invalid value provided")
        step_tps.append(round(token/time,2))
        token_count+=token
        time_count+=time
        cumulative_tps.append(round(token_count/time_count,2))
    overall_tps = round(token_count/time_count,2)
    return {'step_tps' : step_tps,'cumulative_tps' : cumulative_tps,'overall_tps' : overall_tps}
    pass
