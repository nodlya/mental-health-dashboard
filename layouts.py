from dash import html, dcc
from data import mental_df
import plotly.express as px 

df = mental_df
df = df.groupby(['Country']).agg({'Gender': 'count'}).sort_values(by='Gender', ascending=False)
df = df.rename(columns={'Gender': 'Count'})
countries_fig = px.bar(df, x=df.index, y='Count')

general_layout = html.Div([
    html.H2(children='Количество людей по странам', style={'textAlign':'center'}),
    dcc.Graph(id='graph-countries', figure=countries_fig),
    
    html.H2(children='Количество опрошенных по дням', style={'textAlign':'center'}),
    dcc.Dropdown(mental_df.Gender.unique(), mental_df.Gender.unique()[0], id='dropdown-selection'),
    dcc.Graph(id='graph-daily')
])