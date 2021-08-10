
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


# In[34]:


df = crawl_price("0050.TW")
df.Close.plot()


# In[35]:


url = "https://finance.yahoo.com/world-indices/"
response = requests.get(url)

import io
f = io.StringIO(response.text)
dfs = pd.read_html(f)
world_index = dfs[0]


# In[37]:


dfs[0]


# In[ ]:




