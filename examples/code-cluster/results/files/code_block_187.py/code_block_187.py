# normalization
X_scaler_cc = MinMaxScaler()
X_train_cc = X_scaler_cc.fit_transform(train_X_cc)
X_val_cc =  X_scaler_cc.transform(val_X_cc) # intput/output 2D array-like

y_scaler_cc = MinMaxScaler()
y_train_cc = y_scaler_cc.fit_transform(train_y_cc)
y_val_cc = y_scaler_cc.transform(val_y_cc) # array-like