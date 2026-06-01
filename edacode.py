#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install ydata-profiling')
get_ipython().system('pip install pandas numpy')
import pandas as pd
import numpy as np
from ydata_profiling import ProfileReport
df=pd.read_csv("D:\EDA with ydata-profiling\Iris.csv")
profile=ProfileReport(df,title="EDA Report")
profile.to_file("report.html")
profile.to_notebook_iframe()


# In[ ]:




