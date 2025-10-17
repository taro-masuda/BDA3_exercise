#%%
from scipy.stats import binom
print(1 - binom.cdf(k=7, n=12, p=2/3))

#%% 
from scipy.stats import binom
print(1 - binom.cdf(k=7, n=12, p=0.748))
# %%
