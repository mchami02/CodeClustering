categorical_features=['season','month','year','workingday','holiday','weather','hour']
numerical_features=['humidity','windspeed','temp','atemp']
drop_features=['casual','registered','datetime','date','count']
for var in categorical_features:
    data[var]=data[var].astype('category')