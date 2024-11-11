#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sympy as sp
A=sp.Matrix([[1,2,3],[3,4,-1]])
B=sp.Matrix([[2,1],[1,3]])
print("A=",end="")
display(A)
print("B=",end="")
display(B)


# In[2]:


C=B*A
display(C)


# In[4]:


V=sp.Matrix([[1],[2],[3]])
display(V)


# In[5]:


I=C*V
display(I)


# In[6]:


import sympy as sp
A=sp.Matrix([[1,2,4],[3,4,0],[1,-1,1]])
display(A)


# In[12]:


print(A.det())


# In[14]:


D=A.det()
if D!=0:
    display(A.inv())


# In[15]:


T=A.inv()
V=sp.Matrix([1,2,3])
display(V)
print("pre image of V is:")
display(T*V)


# In[ ]:




