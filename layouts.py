from dash import html, dcc
from data import mental_df
from plotly_graphs import countries_fig, pie_fig

general_layout = html.Div([
    
    dcc.Dropdown(mental_df.Timestamp.unique(), mental_df.Timestamp.unique()[0], id='dropdown1'),
    
    html.H2(children='Количество респондентов за день', style={'textAlign':'center'}),
    dcc.Graph(id='indicator1'),
    html.H2(children='% людей долго находящихся дома на указанный день', style={'textAlign':'center'}),
    dcc.Graph(id='indicator2'),
    html.H2(children='% людей, получающих лечение на указанный день', style={'textAlign':'center'}),
    dcc.Graph(id='indicator3'),
    
    html.H2(children='Количество людей по странам', style={'textAlign':'center'}),
    dcc.Graph(id='graph-countries', figure=countries_fig),
    
    html.H2(children='Количество опрошенных по дням', style={'textAlign':'center'}),
    dcc.Dropdown(mental_df.Gender.unique(), mental_df.Gender.unique()[0], id='dropdown-selection'),
    dcc.Graph(id='graph-daily'),
    
    html.H2(children='Доли по наследственности заболеваний', style={'textAlign':'center'}),
    dcc.Graph(id='graph-pie', figure=pie_fig),
    
    html.H2(children='Доли по времени сидения дома', style={'textAlign':'center'}),
    dcc.Dropdown(mental_df.treatment.unique(), mental_df.treatment.unique()[0], id='dropdown-selection-1'),
    dcc.Graph(id='graph-pie-2')
])