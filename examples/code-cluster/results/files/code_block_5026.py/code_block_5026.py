
gb=ensemble.GradientBoostingClassifier()
gb.fit(train_merge4,target)
gb_pre=gb.predict(test_merge4)
accuracy_score(pd.DataFrame(gb.predict(train_merge4)),target)