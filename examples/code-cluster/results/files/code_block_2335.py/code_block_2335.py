data_merged['StoreType'] = data_merged['StoreType'].map({'a':1,'b':2,'c':3,'d':4})
data_merged['StoreType'] = data_merged['StoreType'].astype(int)