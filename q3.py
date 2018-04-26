import pandas as pd
df = pd.read_csv('Crimes_-_2001_to_present.csv')

prop_arrest = (df[df.Arrest]['Primary Type'].value_counts() /
               df['Primary Type'].value_counts())

print(prop_arrest.sort_values().tail(1))
