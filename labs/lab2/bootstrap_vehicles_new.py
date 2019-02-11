import matplotlib
matplotlib.use('Agg')
import pandas as pd
import seaborn as sns
import numpy as np


def bootstrap(sample, sample_size, iterations, ci):
	new_samples = np.empty([0, sample_size])
	means = []
	for j in range(iterations):
		new_sample = np.random.choice(sample, sample_size)
		new_samples = np.vstack((new_samples, new_sample))
		mean = np.mean(new_sample)
		means.append(mean)
	data_mean = np.mean(new_samples)
	lower = np.percentile(means, 50-ci/2.)
	upper = np.percentile(means, 50+ci/2.)
	return data_mean, lower, upper


if __name__ == "__main__":
	df = pd.read_csv('./vehicles.csv')

	data = df.values.T[1]
	data = data[~np.isnan(data)]
	boots = []
	for i in range(100, 50000, 1000):
		boot = bootstrap(data, data.shape[0], i, 95)
		boots.append([i, boot[0], "mean"])
		boots.append([i, boot[1], "lower"])
		boots.append([i, boot[2], "upper"])
		print(i)

	df_boot = pd.DataFrame(boots, columns=['Bootstrap Iterations (New Fleet)', 'Mean', "Value"])
	sns_plot = sns.lmplot(df_boot.columns[0], df_boot.columns[1], data=df_boot, fit_reg=False, hue="Value")

	sns_plot.axes[0, 0].set_ylim(0, )
	sns_plot.axes[0, 0].set_xlim(0, 50000)

	sns_plot.savefig("bootstrap_vehicles_new.png", bbox_inches='tight')
	sns_plot.savefig("bootstrap_vehicles_new.pdf", bbox_inches='tight')

# print ("Mean: %f")%(np.mean(data))
# print ("Var: %f")%(np.var(data))

