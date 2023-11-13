import pandas as pd
path = '/Users/apple/Desktop/Barrior/newCSV/us_weekly_consumable_water_summary_20220102-20230903_1.csv'
df = pd.read_csv(path,usecols=[1, 2])
df.to_csv(r'/Users/apple/Desktop/Barrior/newCSV/us_weekly_consumable_water_summary_20220102-20230903_2.csv',index=False)