#This script creates a data frame from search results.

import requests

import pandas as pd
#Enter your own elsevier API key as a string
apiKey2=
#URL needed to make the json request
url3="https://api.elsevier.com/content/search/scopus"
#Enter your search keyword
query1="CFD"
#Criterion to order the results
sort1="citedby-count"
#Number of results stored in the data frame
count1="150"
#Parameter dictionnary needed to make the json request
params1=dict(query=query1,sort=sort1,apiKey=apiKey2,count=count1,httpAccept="application/json")
#Making the request
test=requests.get(url=url3,params=params1)
#Json request
data=test.json()
#Create the data frame columns
df=data["search-results"]["entry"]

#Final data frame generated
df1=pd.DataFrame(df)
