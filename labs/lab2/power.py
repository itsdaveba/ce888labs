import matplotlib
matplotlib.use('Agg')
import pandas as pd
import seaborn as sns
import numpy as np
from scipy import stats


def power(sample1, sample2, reps, size, alpha):
    counter = 0
    for r in range(reps):
        new_sample1 = np.random.choice(sample1, size)
        new_sample2 = np.random.choice(sample2, size)
        t_stat, p_val = stats.ttest_ind(new_sample1, new_sample2)
        # if p_val < alpha: # Check if this one works better
        if p_val < 1 - alpha:
            counter += 1
    return counter / reps