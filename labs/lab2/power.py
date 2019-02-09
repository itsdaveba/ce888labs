import matplotlib
matplotlib.use('Agg')
import pandas as pd
import seaborn as sns
import numpy as np

def power(sample1, sample2, reps, size, alpha):
    for r in range(reps):
