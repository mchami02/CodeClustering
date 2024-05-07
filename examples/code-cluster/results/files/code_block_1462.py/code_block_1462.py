X_dataset["Date"] = X_dataset["Date"].apply(lambda x:x.replace("-",""))
X_dataset["Date"]  = X_dataset["Date"].astype(int)