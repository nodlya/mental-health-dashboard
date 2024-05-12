import pandas as pd

mental_df = pd.read_csv('data\Mental Health Dataset.csv')
mental_df['Timestamp'] = mental_df['Timestamp'].apply(lambda x: str(x).split(' ', 1)[0])
# print(mental_df.columns)
# df = mental_df[mental_df.Gender == 'Female']
# print(df)
# df = df.groupby(['Timestamp']).agg({'Gender': 'count'})
# print(df)