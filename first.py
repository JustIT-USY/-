#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
data1=[1,2,3,4,5]
array1=np.array(data1)
array1


# In[5]:


data2=[[1,3,4],[2,5,6]]
array2=np.array(data2)
array2


# In[6]:


array2.dtype


# In[7]:


array1.astype('str')


# In[8]:


array1+1


# In[9]:


array1*array1


# In[11]:


array1*2


# In[12]:


array1


# In[13]:


array1[2]


# In[14]:


array1[-2:]


# In[15]:


array1[1]=0
array1


# In[16]:


array2


# In[17]:


array2[0]


# In[18]:


array2[0][1]


# In[20]:


from pandas import Series
x=Series(['a',2,'螃蟹'],index=[1,2,3])
x


# In[21]:


x[3]


# In[22]:


a=Series([1,2,3])
print(a)


# In[23]:


a=Series([1,2,3],index=[1,2,3])
print(a)


# In[25]:


a=Series([1,2,3],index=['A','B','C'])
print(a)


# In[26]:


a=Series([14,26,31])
print(a)
print(a[1])
print(a[5])


# In[27]:


a=Series([14,26,31],index=['first','second','third'])
print(a)
print(a['second'])


# In[35]:


x=Series(['a',True,1],index=['first','second','third'])
x[1]
x['second']
#x[3]
#x.append('2')
n=Series(['2'])
x.append(n)
x=x.append(n)
2 in x.values
'2' in x.values
x[1:3]
x[[0,2,1]]
x.drop(0)
x.drop('first')
x.index[2]
x.drop(x.index[3])
x[2!=x.values]
x[x.index[x.values==True]]='b'
x.index[x.values=='a']
#x.index=[0,1,2,3,4]
#s = Series({'a':1 x.index[x.values=='b'],'b':2,'c':3})


# In[36]:


obj = Series([4.5,7.2,-5.3,3.6],index=['d','b','a','c'])
obj


# In[37]:


obj2=obj.reindex(['a','b','c','d','e'])
obj2


# In[38]:


obj.reindex(['a','b','c','d','e'],fill_value=0)


# In[40]:


from pandas import Series
from pandas import DataFrame
df=DataFrame({ 'age':Series([26,29,24]),'name':Series(['Ken','Jerry','Ben'])},index=[0,1,2])
print(df)


# In[41]:


A=df['age']
print(A)


# In[43]:


B=df[1:2]
print(B)


# In[44]:


C=df.iloc[0:2,0:2]
print(C)


# In[45]:


D=df.at[0,'name']
print(D)


# In[51]:


from pandas import DataFrame
df1=DataFrame({'age':[21,22,23],'name':['KEN','John','JIMI']})
df2=DataFrame(data={'age':[21,22,23],'name':['KEN','John','JIMI']},index=['first','second','third'])
df1[1:100]
print(df1)
df1[2:2]
print(df1)
df1[4:1]
print(df1)
df2['third':'third']
print(df2)
df2['first':'second']
print(df2)
df1['age']
print(df1)
df1[df1.columns[0:1]]
print(df1)
df1.iloc[0:1,0:1]
print(df1)
df1.at[1,'name']
print(df1)
df2.at['second','name']
print(df2)
#df2.at[1,'name']
df1.columns=['age2','name2']
print(df1)
df1.index=range(1,4)
print(df1)
#df1.drop(1,axis=1)
df1.drop('age2',axis=1)
print(df1)
del df1['age2']
print(df1)
df1['newColumn']=[2,4,6]
print(df1)
df2.loc[len(df2)]=[24,'Keno']
print(df2)


# In[52]:


df=DataFrame([[1,2],[3,4]],columns=list('AB'))
df


# In[54]:


df2=DataFrame([[5,6],[7,8]],columns=list('AB'))
df2


# In[55]:


df.append(df2)


# In[56]:


df.append(df2,ignore_index=True)


# In[ ]:




