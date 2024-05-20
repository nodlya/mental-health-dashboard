import plotly.express as px 
from data import countries
from data import pie

countries_fig = px.bar(countries, x=countries.index, y='Count')
pie_fig = px.pie(pie, values='Count', names=pie.index)