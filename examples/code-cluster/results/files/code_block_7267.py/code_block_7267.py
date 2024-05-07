def rmsle(y_test, y_pred):
    return np.sqrt(np.mean((np.log(y_pred+1) - np.log(y_test+1))**2))

reg = LinearRegression()
scorer = make_scorer(rmsle, greater_is_better=False)
reg.fit(x_train, y_train)
y_pred = reg.predict(x_test)
print("RMSLE: " + str(rmsle(y_pred, y_test)))