#!/usr/bin/env python
# coding: utf-8

# In[19]:


import requests 
site = "https://query1.finance.yahoo.com/v7/finance/download/2330.TW?period1=0&period2=1549258857&interval=1d&events=history&crumb=hP2rOschxO0"
response = requests.post(site)
print(response.text)
with open('file.csv','w') as f:
    f.writelines(response.text)
  

    


# In[21]:


import pandas as pd
df = pd.read_csv('file.csv')
print(df.head())


# In[22]:


import pandas as pd
df = pd.read_csv('file.csv', index_col='Date', parse_dates=['Date'])
print(df.head())


# In[24]:


get_ipython().run_line_magic('matplotlib', 'inline')
df.Close.plot()


# In[ ]:




