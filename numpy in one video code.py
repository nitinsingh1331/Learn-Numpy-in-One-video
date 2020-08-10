#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[3]:


b=np.array([[2,3],[4,5],[6,7]])
b


# In[4]:


b.transpose()


# In[5]:


b.dtype


# In[6]:


type(b)


# # maths

# In[10]:


arr=np.arange(1,17).reshape(4,4)
arr1=np.arange(17,33).reshape(4,4)
arr


# In[11]:


arr+arr1


# In[12]:


arr-arr1


# In[13]:


arr*arr1


# In[14]:


arr/arr1


# In[15]:


arr@arr1


# In[16]:


np.sum(arr)


# In[17]:


np.mean(arr)


# In[18]:


np.sqrt(arr)


# In[19]:


np.std(arr)


# In[20]:


np.log(arr)


# # slicing in array

# In[21]:


a=np.arange(1,101).reshape(10,10)
a


# In[22]:


a[0][0]


# In[23]:


a[:]


# In[24]:


a[::]


# In[25]:


a[:,1]


# In[26]:


a[:,0:1]


# In[29]:


arr=np.arange(1,17).reshape(4,4)
arr1=np.arange(17,33).reshape(4,4)
np.concatenate((arr,arr1),axis=1)


# In[30]:


np.vstack((arr,arr1))


# In[31]:


np.hstack((arr,arr1))


# In[32]:


np.hstack((arr,arr,arr1))


# In[33]:


np.sin(180)


# In[34]:


np.cos(45)


# In[35]:


import random


# In[39]:


np.random.random(1)


# In[45]:


np.random.randint(1,3)


# In[46]:


np.random.random((3,3))


# In[47]:


np.random.randint(1,5,(4,4))


# In[48]:


np.random.rand(3)


# In[50]:


np.random.rand(4,4)


# # choice function

# In[57]:


x=["nitin singh","ghaziabad"]
for i in range(10):
    print(np.random.choice(x))


# In[59]:


np.ones(7,dtype=int)


# In[61]:


np.ones((8,8),dtype=int)


# In[62]:


np.zeros(5)


# In[63]:


np.zeros((5,5),dtype=int)


# # strings operations

# In[64]:


f_name="nitin"
l_name="singh"
np.char.upper(f_name)


# In[65]:


np.char.lower(l_name)


# In[66]:


np.char.center(f_name,100)


# In[67]:


np.char.center(f_name,60,fillchar="*")


# In[68]:


np.char.equal(f_name,l_name)


# In[69]:


np.char.find(f_name,"ni")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




