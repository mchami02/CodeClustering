#a = trainHouses[trainHouses["median_house_value"].transform(lambda x: x<=500000)]
#a = trainHouses[trainHouses["median_house_value"] <=500000]
plt.hist(trainHouses[trainHouses["median_house_value"] <=500000]["median_house_value"], bins=100)
plt.show()
culledTrainHouses = trainHouses[trainHouses["median_house_value"] <=500000]
XculledTrainHouses = culledTrainHouses.drop(["Id", "median_house_value"], axis="columns")
YculledTrainHouses = culledTrainHouses.median_house_value
