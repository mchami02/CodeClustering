data_train["Soil_Type"] = data_train["Soil_Type"].apply(lambda x: x.split("Soil_Type")[-1])
data_train.head()