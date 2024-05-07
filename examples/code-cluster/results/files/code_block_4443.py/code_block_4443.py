train['datetime'] = pd.to_datetime(train['datetime'])
train['day'] = train['datetime'].dt.day
train['hour'] = train['datetime'].dt.hour
train['dayofweek'] = train['datetime'].dt.dayofweek
train['month'] = train['datetime'].dt.month
train['year'] = train['datetime'].dt.year
train['weekend'] = (train['dayofweek'] ==5) | (train['dayofweek'] == 6)