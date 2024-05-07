#repeat for registered demand:

X_train, X_test, y_train, y_test = train_test_split(X_Scaled, y_reg, test_size=0.25, random_state=42)

rf_reg=RandomForestRegressor()
rf_reg.fit(X_train,y_train)

importance_reg=pd.DataFrame(rf_reg.feature_importances_ , index=X.columns, columns=['reg']).sort_values(by='reg',ascending=False)
