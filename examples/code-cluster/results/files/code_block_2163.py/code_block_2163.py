test_preds=learn.get_preds(DatasetType.Test)
testdf["Sales"]=np.exp(test_preds[0].data).numpy().T[0]
testdf[["Id","Sales"]]=testdf[["Id","Sales"]].astype("int")
testdf[["Id","Sales"]].to_csv("rossmann_submission.csv",index=False)