#!/usr/bin/env python
# coding: utf-8

# In[12]:


from pandas import read_table
df = read_table(r'C:\Users\12583\Desktop\zero-one\rz.txt',sep=' ')
df.head()


# In[15]:


from pandas import read_csv
df = read_csv(r'C:\Users\12583\Desktop\zero-one\rz.csv',sep=',')
df


# In[35]:


from pandas import read_excel
df = read_excel(r'C:\Users\12583\Desktop\zero-one\rz.xlsx',header=0)
df
#df.to_csv(r'C:\Users\12583\Desktop\zero-one\rz.csv')


# In[31]:


from pandas import DataFrame
from pandas import Series
df = DataFrame({'age':Series([26,85,64]),'name':Series(['Ben','Jehn','Jerry'])})
df


# In[33]:


df.to_csv(r'C:\Users\12583\Desktop\zero-one\01.csv')
df.to_csv(r'C:\Users\12583\Desktop\zero-one\02.csv',index=False)


# In[37]:


from pandas import DataFrame
from pandas import Series
df = DataFrame({'age':Series([26,85,64]),'name':Series(['Ben','John','Jerry'])})
df.to_excel(r'C:\Users\12583\Desktop\zero-one\01.xlsx')
df.to_excel(r'C:\Users\12583\Desktop\zero-one\01.xlsx',index=False)


# In[1]:


from pandas import DataFrame
from pandas import Series
df = DataFrame({'age':Series([26,85,64,85,85]),'name':Series(['Ben','John','Jerry','John','John'])})
df


# In[2]:


df.duplicated()


# In[3]:


df.duplicated('name')


# In[5]:


df.drop_duplicates('age')


# In[6]:


from pandas import DataFrame
from pandas import read_excel
df = read_excel(r'C:\Users\12583\Desktop\zero-one\rz.xlsx')
df


# In[7]:


df.isnull()


# In[8]:


df.notnull()


# In[9]:


newDF=df.dropna()
newDF


# In[12]:


df.fillna('?')


# In[13]:


df.fillna(method='pad')


# In[14]:


df.fillna(method='bfill')


# In[15]:


df.fillna(df.mean())


# In[16]:


df.fillna(df.mean()['高代':'解几'])


# In[17]:


df.fillna({'数分':100,'高代':0})


# In[18]:


from pandas import DataFrame
from pandas import Series
df = DataFrame({'age':Series([26,85,64,85,85]),'name':Series(['Ben','John','Jerry','John','John'])})
df


# In[19]:


df['name'].str.strip()


# In[20]:


df['name'].str.rstrip('n')


# In[ ]:





# In[ ]:




