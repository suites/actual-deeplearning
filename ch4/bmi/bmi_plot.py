import matplotlib.pyplot as plt
import pandas as pd

tbl = pd.read_csv('bmi.csv', index_col=2)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)


def scatter(lbl, color):
    b = tbl.loc[lbl]
    ax.scatter(b['weight'], b['height'], c=color, label=lbl)


scatter('fat', 'red')
scatter('normal', 'yellow')
scatter('thin', 'purple')

ax.legend()
plt.savefig('bmi-test.png')
plt.show()