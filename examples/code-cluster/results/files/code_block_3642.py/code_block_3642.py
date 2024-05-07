test_data = test_dataset.drop(columns = ['datetime', 'atemp'])
test_data = scaler.transform(test_data)
test_data = one_hot.transform(test_data)