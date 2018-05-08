import pandas as pd
df = pd.read_csv('Crimes_-_2001_to_present.csv')

weapon = (df.Description.str.find('WEAPON') >= 0)
arm = (df.Description.str.find('ARM') >= 0)
gun = (df.Description.str.find('GUN') >= 0)
not_no_weapon = (df.Description.str.find('NO WEAPON') == -1)
print(((weapon | arm | gun) & not_no_weapon).mean())
