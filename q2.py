import pandas as pd
df = pd.read_csv('Crimes_-_2001_to_present.csv')

print(df['Primary Type'].value_counts().head(3))
print(df['Primary Type'].value_counts().tail(3))
