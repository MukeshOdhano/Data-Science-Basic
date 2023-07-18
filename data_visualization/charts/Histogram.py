import matplotlib.pyplot as plt
import numpy as np

h1 = np.random.normal(190, 10, 250) # only 3 argument

plt.hist(h1, histtype='stepfilled')
plt.show()


