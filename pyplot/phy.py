import matplotlib as mpl
import matplotlib.pyplot as plt

plt.style.use('classic')

x = [0.2, 0.25, 0.3, 0.35, 0.45, 0.55, 0.6]
y = [1.89, 1.89, 1.87, 1.78, 1.83, 1.88, 1.88]

plt.errorbar(x, y, yerr=0.035, fmt='.k')

plt.show()
