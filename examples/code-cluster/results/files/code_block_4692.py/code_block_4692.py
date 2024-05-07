#Decision Tree with Pruning with 10 Folds
cv = RepeatedKFold(n_splits=10, n_repeats=3, random_state=1)
dtm = DecisionTreeRegressor(random_state=42)
param_grid = {"criterion": ["mse", "mae"],
              "max_depth": [2, 6, 8],
              }
search = GridSearchCV(dtm,param_grid, scoring='neg_mean_squared_error', cv=cv)

results = search.fit(X, Y)
# summarize
print('MSE (NEGATIVE): %.3f' % results.best_score_)
print('Config: %s' % results.best_params_)'