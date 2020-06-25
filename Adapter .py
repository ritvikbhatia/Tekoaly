from fuzzywuzzy import process
import  pandas as pd
t=[]
s=[]
df= pd.read_csv("C:\\Users\\Ritvik\\Desktop\\Tekoaly\\MainGroup1.csv")#new data set
df5= pd.read_csv("C:\\Users\\Ritvik\\Desktop\\Tekoaly\\TestList1 - Copy.csv")#orogonal dataset
choices=list(df5.Desc)
tests=list(df.desc)
for i in range(len(tests)):
    a,b=process.extractOne(tests[i], choices)
    t=t+[a]
    s=s+[b]
df['matched name']=t
df['Score']=s
print(df.head())
