
ada=AdaBoostClassifier()
ada.fit(train_merge4,target)
ada.predict(test_merge4)
accuracy_score(pd.DataFrame(ada.predict(train_merge4)),target)