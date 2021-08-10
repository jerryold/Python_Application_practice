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


# In[27]:


import io
import requests
import datetime
import pandas as pd


def crawl_price(stock_id):
    now=int(datetime.datetime.now().timestamp())+86400
    url = "https://query1.finance.yahoo.com/v7/finance/download/" + stock_id + "?period1=0&period2=" + str(now) + "&interval=1d&events=history&crumb=hP2rOschxO0"
    
    response = requests.post(url)
    f = io.StringIO(response.text)
    df = pd.read_csv(f, index_col='Date', parse_dates=['Date'] )
    
    return df    


# In[28]:


df = crawl_price("0050.TW")
df.Close.plot()


# In[20]:


dfs[0]


# In[19]:


url = "https://finance.yahoo.com/world-indices/"
response = requests.get(url)

import io
f = io.StringIO(response.text)
dfs = pd.read_html(f)
world_index = dfs[0]


# In[23]:


import time
world_index_history = {}
for symbol, name in zip(world_index['Symbol'], world_index['Name']):
    
    print(name)
    world_index_history[name] = crawl_price(symbol)
    time.sleep(5)#不要抓得太頻繁
    


# In[13]:


import matplotlib.pyplot as plt
plt.rcParams['figure.figsize']=(16,9)
plt.style.use('ggplot')
plt.rcParams['image.cmap'] = 'red'
for name, history in world_index_history.items():
    history.Close.plot()


# In[ ]:




