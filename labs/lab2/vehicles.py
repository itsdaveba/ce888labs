import matplotlib
matplotlib.use('Agg')
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

print("Hello World")
df = pd.read_csv('./vehicles.csv')
print(df.columns)
sns_plot = sns.lmplot(df.columns[0], df.columns[1], data=df, fit_reg=False)

sns_plot.axes[0, 0].set_ylim(0,)
sns_plot.axes[0, 0].set_xlim(0,)

sns_plot.savefig("scatter_vehicles.png", bbox_inches='tight')
sns_plot.savefig("scatter_vehicles.pdf", bbox_inches='tight')


data = df.values.T[0]

plt.clf()
sns_plot2 = sns.distplot(data, bins=20, kde=False, rug=True).get_figure()

axes = plt.gca()
axes.set_xlabel('Current fleet')
axes.set_ylabel('Fleet count')

sns_plot2.savefig("histogram_vehicles_current.png", bbox_inches='tight')
sns_plot2.savefig("histogram_vehicles_current.pdf", bbox_inches='tight')


data = df.values.T[1]
data = data[~np.isnan(data)]

plt.clf()
sns_plot3 = sns.distplot(data, bins=20, kde=False, rug=True).get_figure()

axes = plt.gca()
axes.set_xlabel('New fleet')
axes.set_ylabel('Fleet count')

sns_plot3.savefig("histogram_vehicles_new.png", bbox_inches='tight')
sns_plot3.savefig("histogram_vehicles_new.pdf", bbox_inches='tight')
