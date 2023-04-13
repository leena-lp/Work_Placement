import pandas as pd

count1 = 'life_point.csv'

count2 = 'count.csv'

df1 = pd.read_csv(count2)
df2 = pd.read_csv(count1)
print(df1)
print(df2)

final = pd.merge(df1, df2, on='Hospital_id')

final.to_csv('lp.csv')


