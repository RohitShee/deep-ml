import math
def pooled_stats(m1, s1, n1, m2, s2, n2):
    # m1, s1, n1: mean, sample sd, size of group 1
    # m2, s2, n2: mean, sample sd, size of group 2
    # return (combined_mean, combined_sd)
    combined_mean = (m1*n1+m2*n2)/(n1+n2)
    d1 =m1-combined_mean
    d2 =m2 -combined_mean
    combined_sd = math.sqrt(((n1-1)*s1**2+(n2-1)*s2**2+n1*d1**2+n2*d2**2)/(n1+n2-1))
    return combined_mean,combined_sd
    pass