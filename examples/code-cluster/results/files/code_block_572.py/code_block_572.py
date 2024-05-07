from sklearn.preprocessing import LabelEncoder

# Make copy to avoid changing original data 
label_X_train = data_train.copy()
label_X_test = data_test.copy()

# Apply label encoder to each column with categorical data
label_encoder = LabelEncoder()
for col in object_cols:
    label_encoder.fit(pd.concat([data_train[col], data_test[col]], axis=0, sort=False))
    label_X_train[col] = label_encoder.transform(data_train[col])
    label_X_test[col] = label_encoder.transform(data_test[col])