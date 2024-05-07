#data = data.drop('Id', axis=1)
#test_data = test_data.drop('Id', axis=1)
y= data.revenue

x_train = data[data.columns[~data.columns.isin(['Open Date','revenue'])]]  #train features to be fit in model
x_test = test_data[test_data.columns[~test_data.columns.isin(['Open Date'])]]  #test features
