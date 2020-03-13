#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd


# In[ ]:


x = "" #this is the wanted username
y = "" #this is the wanted date


# In[15]:


userdata = pd.read_csv('/Users/mnsguest/Downloads/testing-spiral-graph-classifications.csv') #all data


# In[26]:


#made three new columns: date, time, UTC(idk what UTC is); date is what we want
userdata = pd.read_csv('/Users/mnsguest/Downloads/testing-spiral-graph-classifications.csv') #all data
userdata[["date","time","UTC"]] = userdata.created_at.str.split(expand=True)
# print(userdata)


# In[2]:


#isolate by date and username
def wanted(x,y):
    import pandas as pd
    userdata = pd.read_csv('/Users/mnsguest/Downloads/testing-spiral-graph-classifications.csv') #ogdata
    userdata[["date", "time", "UTC"]] = userdata.created_at.str.split(expand=True)
    ud2 = userdata.loc[userdata["date"] == str(y)]
    ud1 = ud2.loc[ud2["user_name"] == str(x)]
    print(ud1)
wanted(x,y)
    

