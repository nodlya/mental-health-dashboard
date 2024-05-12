from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

from app import app
from data import mental_df

@callback(
    Output('graph-daily', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph_line(value):
    df = mental_df
    if value:
        df = mental_df[mental_df.Gender == value]
    df = df.groupby(['Timestamp']).agg({'Gender': 'count'})
    df = df.rename(columns={'Gender': 'Count'})
    return px.line(df, x=df.index, y='Count')

@callback(
    Output('graph-pie-2', 'figure'),
    Input('dropdown-selection-1', 'value')
)
def update_graph_pie(value):
    df_1 = mental_df
    if value:
        df_1 = mental_df[mental_df.treatment == value]
    df_1 = df_1.groupby(['Days_Indoors']).agg({'Gender': 'count'})
    df_1 = df_1.rename(columns={'Gender': 'Count'})
    return px.pie(df_1, values='Count', names=df_1.index)

if __name__ == '__main__':
    app.run(debug=True) 