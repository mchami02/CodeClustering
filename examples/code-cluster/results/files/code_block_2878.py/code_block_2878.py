y=traindata['ACTION']
x=traindata.drop('ACTION',axis=1)
#Splitting training and testing data
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.70,test_size=0.30, random_state=0)