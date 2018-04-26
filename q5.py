import pandas as pd
df = pd.read_csv('Crimes_-_2001_to_present.csv')

homicides = df[df['Primary Type'] == 'HOMICIDE']
print(homicides['Community Area'].value_counts().head(1))
