import dash
import os
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from plotly import tools
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import pandas as pd
import pandas_profiling
df = pd.read_csv('C:\\Users\\Ritvik\\Desktop\\Tekoaly\\MaxData_2017.csv',encoding='latin-1')
profile = df.profile_report(title='Pandas Profiling Report',output_format='html')
# profile.to_html()
# os.system("start [C:\\Users\\Ritvik\\output.html]")
# locount=[]
# avg=[]
# locount2=[]
# men_bins=[]
# women_bins=[]
# df[' REFBY']=df[' REFBY'].fillna('MAMTA GULATI')
# df.loc[(df[' AGEGR']=='Adult'),' AGE']=df[' AGE'].fillna(31)
# df.loc[(df[' AGEGR']=='Child'),' AGE']=df[' AGE'].fillna(6)
# df.loc[(df[' AGEGR']=='New Born'),' AGE']=df[' AGE'].fillna(0)
# df.loc[(df[' AGEGR']=='Infants'),' AGE']=df[' AGE'].fillna(1)
# locations=df['Location'].unique()
# for i in locations:
#     locount=locount+[(int(df['Location'][df['Location']==i].count()))]
#     locount2=locount2+[(int(df['Location'][df['Location']==i].count()))/50]
#     avg=avg+[(int(df[' AGE'][df['Location']==i].mean()))]
# for i in locations:
#     men_bins=men_bins+[(df['Location'][(df['Location']==i) & (df[' GENDER']=='M')].count())]
#     women_bins=women_bins+[-1*int((df['Location'][(df['Location']==i) & (df[' GENDER']=='F')].count()))]
# y=locations
#
#
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#
# app.layout = html.Div(children=[
#     html.H1(children='Tekoaly'),
#
#     html.Div(children='''
#         Location Based Plots
#     '''),
#
#     dcc.Graph(
#         id='trace1',
#         figure={
#             'data': [
#                 {'x': list(df['Location'].unique()), 'y': locount, 'type': 'bar', 'name': 'SF'}
#             ],
#             'layout': {
#                 'title': 'Number of Patients v/s location plot',
#                 'xaxis':{'title': 'Locations'},
#                 'yaxis':{'title': 'Number of Patients'}
#
#
#             }
#         }
#     ),
#     dcc.Graph(
#         id='example-h',
#         figure={
#             'data': [
#                 {'x': men_bins, 'y': y, 'type': 'bar', 'name': 'MALE','orientation':'h'},
#                 {'x': women_bins, 'y': y, 'type': 'bar', 'name': 'FEMALE','orientation':'h'},
#             ],
#             'layout': {
#                 'title': 'Gender v/s Location Plot',
#                 'xaxis':{'title': 'Number of Patients'},
#                 'barmode':'overlay'
#             }
#         }
#     ),
#
#     dcc.Graph(
#         id='exa',
#
#         figure={
#             'data': [
#                 {'x': locations, 'y': avg, 'type': 'scatter', 'name': 'MALE','orientation':'h','mode':'markers','marker':dict(size=locount2)},
#             ],
#             'layout': {
#                 'title': 'Age v/s Location Plot',
#                 'xaxis':{'title': 'Locations'},
#                 'yaxis':{'title': 'Average Age'}
#             }
#         }
#     )
# ])
#
#
# if __name__ == '__main__':
#     app.run_server(debug=True)
