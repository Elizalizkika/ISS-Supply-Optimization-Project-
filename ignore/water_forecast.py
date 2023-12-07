#copy of water_us.ipynb -> .py in order to function with flask
import pandas as pd
from prophet import Prophet
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error
import matplotlib.pyplot as plt
import base64
from io import BytesIO
import os
import pickle

# Load the data
path = '/Users/eliza/Desktop/us_weekly_consumable_water_summary_20220102-20230903.csv'
data = pd.read_csv(path)
data['Date'] = pd.to_datetime(data['Date'])
prophet_data = data[['Date', 'Corrected Total (L)']].rename(columns={'Date': 'ds', 'Corrected Total (L)': 'y'})

# Split data into training and testing sets (e.g., last 20% as test)
split_index = int(len(prophet_data) * 0.8)
train_data = prophet_data[:split_index]
test_data = prophet_data[split_index:]

# Initialize and train the Prophet model
model = Prophet(
    yearly_seasonality=True, 
    weekly_seasonality=True, 
    daily_seasonality=False,
    seasonality_mode='multiplicative',
    changepoint_prior_scale=0.05 
    )
model.fit(train_data)

# Forecast on the training set and the future
future = model.make_future_dataframe(periods=len(test_data))
forecast = model.predict(future)

# Plot the forecast
fig1 = model.plot(forecast)
plt.title('Water Usage Forecast')
plt.xlabel('Date')
plt.ylabel('Water Usage (L)')

# Show components
fig2 = model.plot_components(forecast)

directory = '/Users/eliza/ISS-Supply-Optimization-Project-/UserInterface/testing/'

fig1_path = os.path.join(directory, 'water_forecast_plot1.png')
fig2_path = os.path.join(directory, 'water_forecast_plot2.png')

fig1.savefig(fig1_path)
fig2.savefig(fig2_path)


'''
previous ideas 
buffer1 = BytesIO()
fig1.savefig(buffer1, format='png')
buffer1.seek(0)
fig1_image_str = base64.b64encode(buffer1.read()).decode('utf-8')
'''


# Error Analysis on Test Data
test_forecast = forecast.iloc[split_index:]
mae = mean_absolute_error(test_data['y'], test_forecast['yhat'])
rmse = np.sqrt(mean_squared_error(test_data['y'], test_forecast['yhat']))
print(f"MAE: {mae}, RMSE: {rmse}")




