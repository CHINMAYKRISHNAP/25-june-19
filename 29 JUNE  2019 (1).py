#!/usr/bin/env python
# coding: utf-8

# In[3]:


# create a series ofnumbers 
import pandas as pd
a=pd.Series([1,3,4,5,6,7])
print(a)


# In[24]:



import numpy as np
a1=pd.Series([1,2,3,4,5,(np.nan)])
print(a1)


# In[14]:


dates=pd.date_range("20190601",periods=5)
print(dates)


# ## 

# In[15]:


a2=pd.DateFrame(np.random.randn(6,4),index=dates,coloumns=list)


# In[23]:


a2=pd.DataFrame({'A':1.,
                 'B':pd.Timestamp('20190601'),
                 'C':pd.Series(1,index=list(range(4)),dtype='float32'),
                 'D':np.array([3]*4,dtype='int32'),
                 'E':pd.Categorical(["test","train","test","train"]),
                 'F':"foo"})
print(a2)


# In[27]:


import Turtle as tt
a1=tt.Turtle()
tt.Forward(100)
tt.done()


# In[ ]:





# In[ ]:




