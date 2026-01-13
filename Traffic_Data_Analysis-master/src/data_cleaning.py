import pandas as pd

def clean_data(data):
    data['Date'] = pd.to_datetime(data['Date'])
    data['Hour'] = data['Date'].dt.hour
    data['Month'] = data['Date'].dt.month
    data['Is_Weekend'] = data['Date'].dt.day_name().isin(['Saturday', 'Sunday'])
    data['Traffic_Signal'] = data['Traffic_Signal'].map({'Yes': 1, 'No': 0})
    return data
