import pandas as pd
df = pd.read_csv('Crimes_-_2001_to_present.csv')

weapon = (df.Description.str.find('WEAPON') > 0)
no_weapon = (df.Description.str.find('NO WEAPON') > 0)
print((weapon & no_weapon).mean())
