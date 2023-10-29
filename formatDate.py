import pandas as pd
path = '/Users/apple/Desktop/Barrior/csv/us_weekly_consumable_water_summary_20220102-20230903.csv'
df = pd.read_csv(path)
df['Date'] = pd.to_datetime(df['Date'])
df.to_csv(r'/Users/apple/Desktop/Barrior/newCSV/us_weekly_consumable_water_summary_20220102-20230903_1.csv', date_format= '%Y-%m-%d')