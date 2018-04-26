import pandas as pd
df = pd.read_csv('Crimes_-_2001_to_present.csv')


prop_arrest = (df[df.Arrest]['Primary Type'].value_counts() /
               df['Primary Type'].value_counts())
crime1000 = df['Primary Type'].value_counts() >= 1000

prop_arrest1000 = prop_arrest[crime1000]
print(prop_arrest1000.sort_values().tail(1))
