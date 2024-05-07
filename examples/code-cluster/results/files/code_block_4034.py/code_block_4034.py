y_casual = np.log1p(train.casual)
y_registered = np.log1p(train.registered)
#y_train = np.log1p(train["count"])

train.drop(["datetime", "windspeed", "casual", "registered", "count"], 1, inplace=True)
test.drop(["datetime", "windspeed", ], 1, inplace=True)