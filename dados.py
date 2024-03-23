import pandas as pd

df = pd.read_csv('Titanic-Dataset.csv', delimiter = ',')
df.head(len(df))
df.plot.bar(x='Survived', y='Age');