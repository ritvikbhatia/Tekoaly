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
avg=[]
df[' REFBY']=df[' REFBY'].fillna('MAMTA GULATI')
df.loc[(df[' AGEGR']=='Adult'),' AGE']=df[' AGE'].fillna(31)
df.loc[(df[' AGEGR']=='Child'),' AGE']=df[' AGE'].fillna(6)
df.loc[(df[' AGEGR']=='New Born'),' AGE']=df[' AGE'].fillna(0)
df.loc[(df[' AGEGR']=='Infants'),' AGE']=df[' AGE'].fillna(1)
locations=df['Location'].unique()
for i in locations:
    locount=locount+[(int(df['Location'][df['Location']==i].count()))/50]
    avg=avg+[(int(df[' AGE'][df['Location']==i].mean()))]

# trace1 = [go.Bar(
#             x=list(df['Location'].unique()),
#             y=locount,
#             name='Number of Patients v/s location plot')]
# layout = go.Layout(
#     title=go.layout.Title(
#         text='Location V/s Patients plot',
#     ),
#     xaxis=go.layout.XAxis(
#         title=go.layout.xaxis.Title(
#             text='Locations',
#         )
#     ),
#     yaxis=go.layout.YAxis(
#         title=go.layout.yaxis.Title(
#             text='Number of patients',
#         )
#     ))
#
# # fig = go.Figure(data=data, layout=layout)
# # plot(fig, filename='basic-bar.html')
# for i in locations:
#     men_bins=men_bins+[(df['Location'][(df['Location']==i) & (df[' GENDER']=='M')].count())]
#     women_bins=women_bins+[-1*int((df['Location'][(df['Location']==i) & (df[' GENDER']=='F')].count()))]
#
# y=locations
# layout = go.Layout(title=go.layout.Title(
#         text='Location V/s Gender plot'),yaxis=go.layout.YAxis(title='Location'),
#                    xaxis=go.layout.XAxis(
#                        range=[-3000, 3000],
#                        title='Number'),
#                    barmode='overlay',
#                    bargap=0.1)
#
# trace2 = [go.Bar(y=y,
#                x=men_bins,
#                orientation='h',
#                name='Men',
#                hoverinfo='x',
#                marker=dict(color='powderblue')
#                ),
#         go.Bar(y=y,
#                x=women_bins,
#                orientation='h',
#                name='Women',
#                text= women_bins,
#                hoverinfo='text',
#                marker=dict(color='seagreen')
#                )]
# fig = tools.make_subplots(rows=1, cols=2)
#
# fig.append_trace(trace2, 1, 1)
# fig.append_trace(trace2, 1, 2)
# fig['layout'].update(height=600, width=800, title='i <3 annotations and subplots')
# plot(fig, filename='bar_pyramid.html')
trace0 = go.Scatter(
    x=locations,
    y=avg,
    mode='markers',
    marker=dict(
        size=locount,
    )
)

data = [trace0]
plot(data, filename='bubblechart-size.html')
