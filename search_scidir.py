# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 17:00:14 2021

@author: flemarchand

This script creates a data frame from search results.
"""
import requests

import pandas as pd
#Number of times cited (scopus)
apiKey2=
url3="https://api.elsevier.com/content/search/scopus"
params1=dict(query="CFD",sort="citedby-count",apiKey=apiKey2,count="150",httpAccept="application/json")
test=requests.get(url=url3,params=params1)
data=test.json()
df=data["search-results"]["entry"]
df1=pd.DataFrame(df)