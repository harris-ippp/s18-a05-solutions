import pandas as pd
df = pd.read_csv('Crimes_-_2001_to_present.csv')

print(len(df))
print(len(df) / 2704958 * 1000)
