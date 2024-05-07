x_train = train.drop(columns=["Id","revenue","Open Date"],axis=1)
y_train = train["revenue"]
x_test = test.drop(columns=["Id","Open Date"],axis=1)
x_train.shape,x_test.shape,y_train.shape