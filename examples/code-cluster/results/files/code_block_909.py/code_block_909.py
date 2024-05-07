from sklearn import linear_model
import numpy 
from sklearn.ensemble import RandomForestRegressor
cls = RandomForestRegressor(n_estimators=100)
cls.fit(X_train, Y_train)
pred = cls.predict(X_test)
pred = numpy.exp(pred)
cls.score(X_train, Y_train)