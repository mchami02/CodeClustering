test_nona = test.dropna().copy()
stores = set(test_nona.Store.values)
test_nona['Sales'] = 0 # create a column to be filled