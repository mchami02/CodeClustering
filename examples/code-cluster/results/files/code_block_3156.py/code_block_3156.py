from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(n_estimators=100, max_depth=19, max_features=11,n_jobs=-1, random_state=42)
clf.fit(x_train, y_train)

y_predicted = clf.predict(x_val)