# Representar la función y  =-2x+5

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 15)
y = -2*x + 5

plt.plot(x, y, color='red', marker='s')
plt.show()