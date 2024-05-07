for var in categorical_feature:
    train[var] = train[var].astype("category")
    test[var] = test[var].astype("category")
train.info()