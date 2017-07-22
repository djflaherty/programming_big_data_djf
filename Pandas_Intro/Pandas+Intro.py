
# coding: utf-8

# In[2]:

import pandas as pd
import numpy as np


# In[3]:

s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])


# In[4]:

s


# In[5]:

s.index


# In[6]:

d = {'a' : 0., 'b' : 1., 'c' : 2.}


# In[7]:

pd.Series(d)


# In[8]:

pd.Series(5., index=['a', 'b', 'c', 'd', 'e'])


# In[9]:

s


# In[10]:

s[0]


# In[11]:

s[s > s.median()]


# In[12]:

s[[4, 3, 1]]


# In[13]:

np.exp(s)


# In[14]:

s['a']


# In[15]:

s['a']


# In[16]:

s['e'] = 12.


# In[17]:

s


# In[18]:

if 'f' in s:
    s['f']


# In[19]:

s + s


# In[20]:

something = pd.Series(np.random.randn(5))


# In[21]:

something


# In[22]:

something['f']=0


# In[23]:

something


# In[24]:

d = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
     'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}


# In[27]:

d


# In[25]:

df = pd.DataFrame(d)


# In[26]:

df


# In[28]:

pd.DataFrame(d, index=['d', 'b', 'a'])


# In[34]:

data = np.zeros((2,), dtype=[('A', 'i4'),('B', 'f4'),('C', 'a10')])


# In[30]:

data


# In[35]:

pd.DataFrame(data, index=['first', 'second'])


# In[36]:

data = np.zeros((2,), dtype=[('A', 'i4'),('B', 'f4'),('C', 'a10')])


# In[37]:

data[:] = [(1,2.,'Hello'), (2,3.,"World")]


# In[38]:

pd.DataFrame(data)


# In[39]:

pd.DataFrame(data, index=['first', 'second'])


# In[40]:

pd.DataFrame(data, columns=['C', 'A', 'B'])


# In[41]:

data2 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]


# In[42]:

pd.DataFrame(data2)


# In[43]:

pd.DataFrame(data2, index=['first', 'second'])


# In[44]:

pd.DataFrame(data2, columns=['a', 'b'])


# In[45]:

df


# In[46]:

df['one']


# In[47]:

df['three'] = df['one'] * df['two']


# In[48]:

df


# In[49]:

df['flag'] = df['one'] > 2


# In[50]:

df


# In[51]:

three = df.pop('three')


# In[52]:

three


# In[ ]:



