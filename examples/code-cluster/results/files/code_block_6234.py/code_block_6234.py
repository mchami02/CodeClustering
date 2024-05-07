from sklearn.ensemble import RandomForestRegressor

rgr = RandomForestRegressor(n_estimators=25, verbose=True, n_jobs=8)
rgr.fit(X_train, y_train)
print(rgr.score(X_train, y_train))