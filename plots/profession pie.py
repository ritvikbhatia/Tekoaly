import plotly.graph_objs as go
from plotly import tools
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import pandas as pd
import pandas_profiling
df = pd.read_csv('C:\\Users\\Ritvik\\Desktop\\Tekoaly\\MaxData_2017.csv',encoding='latin-1')
# profile = df.profile_report(title='Pandas Profiling Report')
# profile.to_html()
locount=[]
locountm=[]
men_bins=[]
women_bins=[]
ag=[]
# df[' REFBY']=df[' REFBY'].fillna('MAMTA GULATI')
df.loc[(df[' AGEGR']=='Adult'),' AGE']=df[' AGE'].fillna(31)
df.loc[(df[' AGEGR']=='Child'),' AGE']=df[' AGE'].fillna(6)
df.loc[(df[' AGEGR']=='New Born'),' AGE']=df[' AGE'].fillna(0)
df.loc[(df[' AGEGR']=='Infants'),' AGE']=df[' AGE'].fillna(1)
locations=df['Location'].unique()
for i in locations:
    locount=locount+[(int(df['Location'][df['Location']==i].count()))/50]
labels = list(df['Profession'].unique())
for i in labels:
    ag=ag+[df['Profession'][df['Profession']==i].count()]
values = ag

trace = go.Pie(labels=labels, values=values)

plot([trace], filename='basic_pie_chart.html')
