from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

from app import app
from data import mental_df

@callback(
    Output('graph-daily', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph_2(value):
    df = mental_df
    if value:
        df = mental_df[mental_df.Gender == value]
    df = df.groupby(['Timestamp']).agg({'Gender': 'count'})
    df = df.rename(columns={'Gender': 'Count'})
    return px.line(df, x=df.index, y='Count')


if __name__ == '__main__':
    app.run(debug=True) 