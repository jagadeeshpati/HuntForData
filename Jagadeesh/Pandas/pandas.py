
# coding: utf-8

# # Pandas is a core package with additional features from a variety of other packages.

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv('iris.csv')


# In[3]:


data.to_csv('created_file.csv', index = None)


# ## index=None will simply write the data as it is. 
# ###If you don’t write index=None, you’ll get an additional first column of 1,2,3, … until the last row.

# In[4]:


data.shape


# In[5]:


data.describe


# In[6]:


data.head(3)


# In[7]:


data.loc[8]


# In[8]:


#print the value of 8th row and column one
data.loc[8, 'SepalLength']


# In[9]:


data.loc[range(4,6)]


# In[10]:


data['SepalLength'].plot()


# In[11]:


data['SepalLength'].hist()


# ### Updating the data

# In[12]:


# Change values of multiple rows in one line
data.loc[data['Name']=='Iris-setosa', 'Name']='Iris-Setosa'


# In[13]:


data['Name']


# In[14]:


data['Name'].value_counts()


# ### Operations on full rows, columns, or all data

# In[15]:


data['Name'].map(len)


# In[16]:


'''A great pandas feature is the chaining method. 
It helps you do multiple operations (.map() and .plot() here) in one line, for more simplicity and efficiency'''

data['Name'].map(len).map(lambda x: x/100).plot()


# ### correlation and scatter matrices

# In[18]:


data.corr()


# In[19]:


data.corr().applymap(lambda x: int(x*100)/100)


# In[20]:


pd.plotting.scatter_matrix(data, figsize=(12,8))


# ## Advanced operations in pandas

# ### The SQL Joins

# In[22]:


# Joining on 3 columns takes just one line
# data.merge(other_data, on=['column_1', 'column_2', 'column_3'])


# In[23]:


data.groupby('Name')['SepalWidth'].apply(sum).reset_index()


# In[25]:


# Iterating over rows

dictionary = {}

for i,row in data.iterrows():
  dictionary[row['Name']] = row['PetalLength']

