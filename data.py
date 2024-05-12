import pandas as pd


mental_df = pd.read_csv('data\Mental Health Dataset.csv')
mental_df['Timestamp'] = mental_df['Timestamp'].apply(lambda x: str(x).split(' ', 1)[0])

countries = mental_df.groupby(['Country']).agg({'Gender': 'count'}).sort_values(by='Gender', ascending=False)
countries = countries.rename(columns={'Gender': 'Count'})

pie = mental_df.groupby('Mental_Health_History').agg({'Gender': 'count'})
pie = pie.rename(columns={'Gender': 'Count'})

