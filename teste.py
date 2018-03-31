import numpy as np
import matplotlib.pyplot as plt
import time
plt.ion()
for i in range(3):
    plt.plot(np.random.rand(10))
    plt.show()
    plt.pause(1e-10)