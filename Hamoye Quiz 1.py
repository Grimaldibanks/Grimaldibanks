#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


url = 'https://raw.githubusercontent.com/ooseni/Hamoye-Datasets/main/FoodBalanceSheets_E_Africa_NOFLAG%20(2).csv'


# In[3]:


food_balance_data = pd.read_csv(url, sep=',', encoding='latin-1')
food_balance_data.describe(include='all')


# In[4]:


sum(count)


# In[5]:


df=pd.read_excel('/users/BUSOLA/Downloads/FoodBalanceSheets_E_Africa_NOFLAG.xlsx')
df.head()


# In[6]:


gk=df.groupby('Item')


# In[7]:


gk.first()


# In[8]:


gk.get_group('Animal fats')


# In[9]:


gk=df.groupby('Element')


# In[10]:


gk.first


# In[11]:


gk.first()


# In[12]:


gk.sum('Import Quan')


# In[13]:


gk.groupby('Area')


# In[14]:


gk=df.groupby('Area')


# In[15]:


gk.first()


# In[16]:


gk.count('Area')


# In[23]:


gk=df.groupby('Item')
gk.first()


# In[24]:


gk.sum('Item')


# In[ ]:




