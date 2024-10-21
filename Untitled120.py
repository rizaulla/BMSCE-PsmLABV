#!/usr/bin/env python
# coding: utf-8

# In[12]:


import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import geom
gd=geom.rvs(p=0.6,size=1000)
vg = sns.displot(gd,kde= False, color ="skyblue",alpha = 1)
vg.set(xlabel='Number of Trials required  to obtaion the first success', ylabel = 'Frequency', title= "Histogram of geometric Distribution")
print(gd)
plt.show(vg)
print("MEAN=",np.mean(gd))
print("Variance=",np.var(gd))


# In[13]:


from scipy.stats import binom
prob=binom.pmf(10,n=10,p=0.15)
prob2=binom.pmf(3,n=20,p=0.15)
print(prob)
print(prob2)


# In[14]:


from scipy.stats import poisson
p=poisson.cdf(499,mu=50)
print(p)


# In[20]:


import seaborn as sns
from scipy.stats import poisson
d=poisson.rvs(mu=5,size=1000)
plot=sns.displot(d,kde=False,color='blue',alpha=1)
plot.set(xlabel='Number of Trials required  to obtaion the first success', ylabel = 'Frequency', title= "Histogram of geometric Distribution")
plt.show(d)


# In[ ]:




