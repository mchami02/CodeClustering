traindf = pd.read_csv("../input/train.csv", low_memory=False)
traindf = f(traindf)
traindf = traindf[traindf.Open == 1]
ytrain = traindf.Sales.values
del traindf ["Sales"]
del traindf ["Customers"]
del traindf ["Open"]

traindf.head()