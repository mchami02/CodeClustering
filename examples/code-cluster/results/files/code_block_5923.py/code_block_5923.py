submission = pd.DataFrame({<br>        "listing_id": index,<br>        "high": test_predictions[:,0],<br>        "medium":test_predictions[:,2],<br>        "low":test_predictions[:,1]<br>    })<br>    <br>columnsTitles=["listing_id","high","medium","low"]<br>submission=submission.reindex(columns=columnsTitles)<br>submission.to_csv(\'submission.csv\', index=False)