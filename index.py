from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.graph_objects as go

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

@callback(
    Output('indicator1', 'figure'),
    Input('dropdown1', 'value')
)
def update_indicator_1(value):
    filtered_df = mental_df[mental_df['Timestamp'] == value]
    value_count = filtered_df.shape[0]
    
    fig = go.Figure(go.Indicator(
        mode = "number",
        value = value_count,
        domain = {'row': 0, 'column': 1})
    )
    
    fig.update_layout(
        paper_bgcolor="#E7EBFD",
        height=250,
    )
    
    return fig

@callback(
    Output('indicator2', 'figure'),
    Input('dropdown1', 'value')
)
def update_indicator_2(value):
    filtered_df = mental_df[mental_df['Timestamp'] == value]
    value_count = round(filtered_df[filtered_df['Days_Indoors'] == filtered_df['Days_Indoors'].values[-1]].shape[0]/filtered_df.shape[0]*100, 2)
    
    
    fig = go.Figure(go.Indicator(
        mode = "number",
        value = value_count,
        domain = {'row': 0, 'column': 1})
    )
    
    fig.update_layout(
        paper_bgcolor="#E7EBFD",
        height=250,
    )
    
    return fig

@callback(
    Output('indicator3', 'figure'),
    Input('dropdown1', 'value')
)
def update_indicator_3(value):
    filtered_df = mental_df[mental_df['Timestamp'] == value]
    value_count = round(filtered_df[filtered_df['treatment'] == filtered_df['treatment'].values[-1]].shape[0]/filtered_df.shape[0]*100, 2)
    
    fig = go.Figure(go.Indicator(
        mode = "number",
        value = value_count,
        domain = {'row': 0, 'column': 1})
    )
    
    fig.update_layout(
        paper_bgcolor="#E7EBFD",
        height=250,
    )
    
    return fig

if __name__ == '__main__':
    app.run(debug=True) 