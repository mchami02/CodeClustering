# Test Set Predictions
test_proba = clf.predict_proba(test)
test_preds = test_proba[:,1]
test_res=clf.predict(test)

# Format for submission
output = pd.DataFrame({ 'activity_id' : test_ids, 'outcome': test_preds })
output1 = pd.DataFrame({ 'activity_id' : test_ids, 'outcome': test_res })
output.head()