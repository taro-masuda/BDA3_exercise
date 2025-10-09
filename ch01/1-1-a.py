#%%
import numpy as np
import matplotlib.pyplot as plt

def norm_dist(x: np.ndarray, mu: float, sigma: float) -> np.ndarray:
    return 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(- 1./2 * ((x - mu) / sigma) **2)

#%% 
x = np.linspace(-10, 10, 1000)
y1 = norm_dist(x, 1, 2)
y2 = norm_dist(x, 2, 2)

y = 1/2 * y1 + 1/2 * y2
plt.plot(x, y)
plt.show()
# %%
