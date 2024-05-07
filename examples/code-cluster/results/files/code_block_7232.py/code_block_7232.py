forest = RandomForestRegressor(max_depth=21, random_state=0, n_estimators=1000)
forest.fit(Xtrain3, Ytrain)

Ypred = forest.predict(Xtrain3)
forest_rmsle = rmsle(Ytrain, Ypred)

print('log error =', forest_rmsle)

prediction = forest.predict(Xtest2)