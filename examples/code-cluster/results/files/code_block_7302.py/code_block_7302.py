from sklearn import neighbors

knn = neighbors.KNeighborsRegressor(n_neighbors=6)
knn.fit(X_train_scaled, Y)
knn_scores = cross_val_score(knn, X_train_scaled, Y, cv=10)

np.mean(knn_scores)