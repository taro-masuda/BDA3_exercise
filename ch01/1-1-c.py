#%%
import numpy as np
import matplotlib.pyplot as plt

def func(x: np.ndarray, sigma: float) -> np.ndarray:
    return 1 / (1 + np.exp(-x / sigma))

#%% 
x = np.linspace(-10, 10, 1000)
y1 = func(x, 0.01)
y2 = func(x, 0.1)
y3 = func(x, 10)
y4 = func(x, 100)

plt.plot(x, y1, label="sigma=0.01")
plt.plot(x, y2, label="sigma=0.1")
plt.plot(x, y3, label="sigma=10")
plt.plot(x, y4, label="sigma=100")
plt.legend()
plt.show()
# %%
