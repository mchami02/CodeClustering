X_train = train.drop(['Id','Cover_Type','soil_type','Wilderness_Area'], axis = 1)
y_train = train.Cover_Type
X_test = test.drop(['Id'], axis = 1)