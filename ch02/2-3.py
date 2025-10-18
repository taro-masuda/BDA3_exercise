#%%
import numpy as np
import matplotlib.pyplot as plt

def norm_dist(x: np.ndarray, mu: float, sigma: float) -> np.ndarray:
    return 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(- 1./2 * ((x - mu) / sigma) **2)

#%% 
x = np.linspace(0, 300, 1000)
y = norm_dist(x, 1000/6, np.sqrt(1000/6 * 5/6))

plt.plot(x, y)
plt.show()
# %%
from scipy.stats import norm
l = [norm.ppf(x)*np.sqrt(1000/6 * 5/6) + 1000/6 for x in [0.05, 0.25, 0.5, 0.75, 0.95]]
print([float(x) for x in l])
# %%
