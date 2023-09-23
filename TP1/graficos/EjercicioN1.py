# Representar la función y = x^2+2x-2

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 20)

y = x**2 + 2 * x - 2

plt.plot(x, y, color='blue', marker='o')
plt.title('y = x^2+2x-2')
plt.grid(linestyle='dotted')
plt.show()