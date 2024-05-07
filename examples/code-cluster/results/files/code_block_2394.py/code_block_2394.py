submission = pd.read_csv('/kaggle/input/rossmann-store-sales/sample_submission.csv')
submission_predicted = pd.DataFrame({'Id':test['Id'],'Sales':test_pred_inv})
submission_predicted.to_csv('submission.csv',index=False)
submission_predicted.head()