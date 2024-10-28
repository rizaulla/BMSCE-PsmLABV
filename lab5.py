#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math

n=365
k=1
x=[]

for i in range(n,0,-1):
    j=i/365
    x.append(j)
    k=math.prod(x)
    if k<=0.5:
        break

len(x)

