from sklearn.preprocessing import MinMaxScaler
minmaxscaler = MinMaxScaler()
col_inds = [0,1,4,5,6,7,8,10,11,12] # 0,1 [0,1,3,4,5,6,7,8,9,10,13] 2 [0,1,3,4,5,6,7,8,9,10,11,12,13] 3 [0,1,4,5,6,7,8,10,11,12]
Xadult_unscaled = adult_fill.iloc[:,col_inds].apply(LabelEncoder().fit_transform)
Xadult = minmaxscaler.fit_transform(Xadult_unscaled)
Yadult = adult_fill.income
print(Xadult_unscaled.columns.values)