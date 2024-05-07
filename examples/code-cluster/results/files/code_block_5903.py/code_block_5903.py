clf = LogisticRegression(C=0.08)#, multi_class='multinomial',solver='lbfgs')
clf.fit(Xtrain[70001:], y[70001:])
pred = pd.DataFrame(clf.predict_proba(Xtrain[70001:]), index=gatrain.iloc[70001:].index, columns=targetencoder.classes_)
pred.head()