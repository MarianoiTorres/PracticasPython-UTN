# Para “románticos”, representar gráficamente un corazón (ecuación cardioide).

import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 9, 100)

r = 1 * (1 - np.sin(theta))

plt.figure(figsize=(6, 6))
plt.polar(theta, r, color='red', lw=2)

plt.title('Ecuación cardioide')

plt.show()