data_train["Wilderness_Area"] = data_train[features_wilderness].apply(np.argmax, axis=1)
data_train["Wilderness_Area"] = data_train["Wilderness_Area"].apply(lambda x: x.split("Wilderness_Area")[-1])
data_train.Wilderness_Area.head()