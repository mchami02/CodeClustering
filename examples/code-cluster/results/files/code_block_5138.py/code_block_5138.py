from sklearn.preprocessing import LabelEncoder

train_users_n = train_users.shape[0]
X_train = all_users.values[:train_users_n]
le = LabelEncoder()
y_train = le.fit_transform(labels)   
X_test = all_users.values[train_users_n:]